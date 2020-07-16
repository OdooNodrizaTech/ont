# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    @api.multi
    def button_confirm(self):
        # action_confirm
        return_data = super(PurchaseOrder, self).button_confirm()
        # operations
        for item in self:
            if item.state == 'purchase':
                for picking_id in item.picking_ids:
                    picking_id.purchase_id = item.id
        # return
        return return_data