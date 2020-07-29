# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api,  models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.multi
    def cron_action_regenerate_purchase_prices(self):
        return_object = super(SaleOrder, self).cron_action_regenerate_purchase_prices()
        for item in self:
            if item.invoice_ids:
                for invoice_id in item.invoice_ids:
                    invoice_id.action_regenerate_margin()
        # return
        return return_object
