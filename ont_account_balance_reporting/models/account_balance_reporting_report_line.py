# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
import logging
_logger = logging.getLogger(__name__)

from openerp import api, models, fields
from openerp.exceptions import Warning
import operator

class AccountBalanceReportingLine(models.Model):
    _inherit = 'account.balance.reporting.line'                
    
    @api.one
    @api.depends('current_move_line_ids')    
    def get_current_acount_account_ids(self):        
        current_acount_account_ids = False
        current_acount_account_ids_new = False            
        
        if len(self.child_ids)==0:        
            skip = False
            
            if self.template_line_id.current_value!=False:
                if '+' in self.template_line_id.current_value:
                    skip = True
            
            if self.template_line_id.previous_value!=False:                
                if '+' in self.template_line_id.previous_value:
                    skip = True                
            
            if skip==False:
                if len(self.current_move_line_ids)>0:
                    current_acount_account_ids = {}
                    account_ids = []
                    
                    balance_mode = self.template_line_id.template_id.balance_mode                    
                    
                    for current_move_line_id in self.current_move_line_ids:
                        if not current_move_line_id.account_id.id in account_ids:
                            current_acount_account_ids[current_move_line_id.account_id.id] = {
                                'account_id': current_move_line_id.account_id.id,
                                'code': current_move_line_id.account_id.code,
                                'name': current_move_line_id.account_id.name,
                                'current_value': 0
                            }
                            account_ids.append(current_move_line_id.account_id.id)
                        #sum values
                        current_value_item = 0
                        
                        if balance_mode=='0':
                            current_value_item = current_move_line_id.debit-current_move_line_id.credit
                        elif balance_mode=='1':#in brackets
                            current_value_item = current_move_line_id.debit-current_move_line_id.credit
                        elif balance_mode=='2':
                            current_value_item = current_move_line_id.credit-current_move_line_id.debit
                        elif balance_mode=='3':#in brackets
                            current_value_item = current_move_line_id.credit-current_move_line_id.debit
                            
                        if self.template_line_id.negate==True:
                            current_value_item = current_value_item*-1                                                                                    

                        current_acount_account_ids[current_move_line_id.account_id.id]['current_value'] += current_value_item
                        current_acount_account_ids[current_move_line_id.account_id.id]['current_value'] = float("{0:.2f}".format(current_acount_account_ids[current_move_line_id.account_id.id]['current_value']))
                                                                                                                                                                   
                #current_acount_account_ids_sorted
                if current_acount_account_ids!=False:
                    current_acount_account_ids_sorted = []
                    for current_acount_account_id in current_acount_account_ids:
                        current_acount_account_id_item = current_acount_account_ids[current_acount_account_id]
                        current_acount_account_ids_sorted.append(current_acount_account_id_item)
                        
                    current_acount_account_ids_sorted = sorted(current_acount_account_ids_sorted, key=operator.itemgetter('code'))
                    #current_acount_account_ids_new
                    current_acount_account_ids_new = []
                    for current_acount_account_id_sorted in current_acount_account_ids_sorted:                    
                        current_acount_account_ids_new.append({
                            'account_id': current_acount_account_id_sorted['account_id'],
                            'code': current_acount_account_id_sorted['code'],
                            'name': current_acount_account_id_sorted['name'],
                            'current_value': current_acount_account_id_sorted['current_value']
                        })                    
                        
        return current_acount_account_ids_new                                                        