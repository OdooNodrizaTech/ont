# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models, fields


class AccountInvoiceLine(models.Model):
    _inherit = 'account.invoice.line'

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
            if item.margin != 0 and item.price_subtotal > 0:
                margin_line_percent = (item.margin / item.price_subtotal) * 100
                item.margin_percent = "{:.2f}".format(margin_line_percent)
