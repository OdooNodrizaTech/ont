# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
import logging
_logger = logging.getLogger(__name__)

from openerp import api, models, fields
from openerp.exceptions import Warning

class ResBank(models.Model):
    _inherit = 'res.bank'
    
    public_name = fields.Char(
        string='Nombre publico'
    )