# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    picking_note = fields.Text(
        string='Picking note',
    )

    def _create_delivery_line(self, carrier, price_unit):
        if price_unit > 0:
            return super(SaleOrder, self)._create_delivery_line(carrier, price_unit)