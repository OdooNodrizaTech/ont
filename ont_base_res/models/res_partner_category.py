# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from openerp import api, models, fields
from openerp.exceptions import Warning, ValidationError

import re

import logging
_logger = logging.getLogger(__name__)

class ResPartnerCategory(models.Model):
    _inherit = 'res.partner.category'    
    _order = 'position'
    
    position = fields.Integer(
        string='Posicion'
    ) 