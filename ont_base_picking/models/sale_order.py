# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from openerp import api, models, fields
from openerp.exceptions import Warning

import logging
_logger = logging.getLogger(__name__)

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    picking_note = fields.Text(
        string='Nota albaran',
    )

    def _create_delivery_line(self, carrier, price_unit):
        if price_unit > 0:
            return super(SaleOrder, self)._create_delivery_line(carrier, price_unit)