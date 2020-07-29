# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    @api.multi
    @api.onchange('product_id')
    def onchange_product_id_override(self):
        for item in self:
            if item.product_id:
                if item.product_id.default_code:
                    if item.product_id.default_code in item.name:
                        item.name = item.name.split(']')[1]
