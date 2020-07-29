# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models, fields


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    margin_percent = fields.Float(
        string='Margin %'
    )

    @api.multi
    def action_calculate_margin_percent(self):
        for item in self:
            item.margin_percent = 0
            if item.margin != 0 and item.price_subtotal > 0:
                margin_percent = (item.margin / item.price_subtotal) * 100
                item.margin_percent = "{:.2f}".format(margin_percent)
