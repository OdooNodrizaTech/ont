# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import api, models, fields

import logging
_logger = logging.getLogger(__name__)

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    picking_note = fields.Char(
        string='Nota albaran',
    )

    def _create_delivery_line(self, carrier, price_unit):
        if price_unit > 0:
            return super(SaleOrder, self)._create_delivery_line(carrier, price_unit)

    @api.multi
    def action_confirm(self):
        return_data = super(SaleOrder, self).action_confirm()
        # operations
        for item in self:
            if item.state == 'sale':
                for picking_id in item.picking_ids:
                    picking_id.sale_order_note = item.picking_note
        # return
        return return_data