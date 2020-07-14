# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
import logging
_logger = logging.getLogger(__name__)

from openerp import api, models, fields
from openerp.exceptions import Warning
import odoo.addons.decimal_precision as dp

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'
            
    @api.onchange('product_id')
    def onchange_product_id_override(self):
        if self.product_id.id>0:
            if self.product_id.default_code!=False:
                if self.product_id.default_code in self.name:
                    name_split = self.name.split(']')
                    self.name = name_split[1]