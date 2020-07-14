# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import api, fields, models

import logging
_logger = logging.getLogger(__name__)

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    @api.one    
    def cron_action_regenerate_purchase_prices(self):
        return_object = super(SaleOrder, self).cron_action_regenerate_purchase_prices()
        #invoices (regenerate_margin)
        if self.invoice_ids!=False:
            for invoice_id in self.invoice_ids:
                invoice_id.action_regenerate_margin()
        #return
        return return_object