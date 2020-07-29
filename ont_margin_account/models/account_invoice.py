# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models, fields


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    margin = fields.Float(
        string='Margin'
    )
    margin_percent = fields.Float(
        string='Margin %'
    )

    @api.multi
    def action_calculate_margin_percent(self):
        for item in self:
            item.margin_percent = 0
            if item.margin != 0 and item.amount_untaxed > 0:
                margin_percent = (item.margin / item.amount_untaxed) * 100
                item.margin_percent = "{:.2f}".format(margin_percent)

    @api.multi
    def action_invoice_open(self):
        for item in self:
            item.action_regenerate_margin()
        return super(AccountInvoice, self).action_invoice_open()

    @api.multi
    def action_regenerate_margin_multi(self):
        for item in self:
            item.action_regenerate_margin()

    @api.multi
    def action_regenerate_margin(self):
        for item in self:
            if item.type in ['out_invoice', 'out_refund']:
                if item.state in ['open', 'paid']:
                    if item.invoice_line_ids:
                        margin = 0
                        # operations
                        if item.type == 'out_invoice':
                            for line_id in item.invoice_line_ids:
                                margin_line = 0
                                # invoice_line_id
                                if line_id.sale_line_ids:
                                    for sale_line_id in line_id.sale_line_ids:
                                        margin_line += sale_line_id.margin
                                else:
                                    if item.invoice_line_id.product_id:
                                        margin_line = \
                                            line_id.price_subtotal - \
                                            (item.invoice_line_id.product_id.standar_price
                                             * line_id.quantity)
                                # margin_line
                                line_id.margin = "{:.2f}".format(margin_line)
                                # action_calculate_margin_percent
                                line_id.action_calculate_margin_percent()
                                # margin
                                margin += margin_line
                        else:  # out_refund
                            if item.origin:
                                items = self.env['account.invoice'].search(
                                    [
                                        ('number', '=', item.origin)
                                    ]
                                )
                                if items:
                                    org_invoice = items[0]
                                    # invoice_line_ids
                                    for line_id in item.invoice_line_ids:
                                        margin_line = 0
                                        # search in origin invoice
                                        for org_invoice_line \
                                                in org_invoice.invoice_line_ids:
                                            if org_invoice_line.product_id.id \
                                                    == line_id.product_id.id:
                                                # buscamos el coste del PV del que viene
                                                purchase_price_line = 0
                                                for sale_line_id \
                                                        in org_invoice_line.sale_line_ids:
                                                    purchase_price_line = \
                                                        sale_line_id.purchase_price
                                                # calculamos el margen de esta linea
                                                margin_line = \
                                                    line_id.price_subtotal -\
                                                    (purchase_price_line
                                                     * invoice_line.quantity)
                                        # margin_line
                                        line_id.margin = "{:.2f}".format(margin_line)
                                        # action_calculate_margin_percent
                                        line_id.action_calculate_margin_percent()
                                        # margin
                                        margin += margin_line
                        # margin
                        item.margin = "{:.2f}".format(margin)
                        # action_calculate_margin_percent
                        item.action_calculate_margin_percent()
