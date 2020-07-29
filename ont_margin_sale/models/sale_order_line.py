# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models, fields


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    margin_percent = fields.Float(
        string='Margin %'
    )

    @api.multi
    def action_calculate_margin_percent(self):
        self.ensure_one()
        self.margin_percent = 0
        if self.margin != 0 and self.price_subtotal > 0:
            margin_percent = (self.margin / self.price_subtotal) * 100
            self.margin_percent = "{:.2f}".format(margin_percent)
