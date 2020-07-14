# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
import logging
_logger = logging.getLogger(__name__)

from odoo import api, models, fields
from odoo.exceptions import Warning

class AccountInvoice(models.Model):
    _inherit = 'account.invoice'
    
    inv_vat = fields.Char(
        string='VAT',
        related='partner_id.vat'
    )
    partner_bank_name = fields.Char(
        compute='_partner_bank_name',
        string='Banco'
    )
    
    @api.multi        
    def _partner_bank_name(self):
        for obj in self:
            obj.partner_bank_name = ''
            if obj.partner_bank_id.id>0:
                if obj.partner_bank_id.bank_id.id>0:
                    obj.partner_bank_name = obj.partner_bank_id.bank_id.name + ' ' + obj.partner_bank_id.acc_number[-4:]
                else:
                    obj.partner_bank_name = obj.partner_bank_id.acc_number