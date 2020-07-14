# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
import logging
_logger = logging.getLogger(__name__)

from odoo import api, models, fields

class AccountBankStatementLine(models.Model):
    _inherit = 'account.bank.statement.line'
    
    @api.multi
    def get_move_lines_for_reconciliation_widget(self, excluded_ids=None, str=False, offset=0, limit=None):
        return_item =  super(AccountBankStatementLine, self).get_move_lines_for_reconciliation_widget(excluded_ids, str, offset, limit)
        #operations (reverse)
        if len(return_item)>0:
            return_item = list(reversed(return_item))
        #return
        return return_item        