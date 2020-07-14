# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
import logging
_logger = logging.getLogger(__name__)

from odoo import api, models, fields
from odoo.exceptions import Warning

class AccountFiscalPosition(models.Model):
    _inherit = 'account.fiscal.position'
    
    invoice_description = fields.Text(
        string='Descripcion en factura'
    )