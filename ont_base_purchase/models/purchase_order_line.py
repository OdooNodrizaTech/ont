# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    @api.onchange('product_id')
    def onchange_product_id_override(self):
        if self.product_id:
            if self.product_id.default_code:
                if self.product_id.default_code in self.name:
                    self.name = self.name.split(']')[1]
