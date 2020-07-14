# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
import logging
_logger = logging.getLogger(__name__)

from odoo import api, models, fields

class AccountInvoice(models.Model):
    _inherit = 'account.invoice'
        
    margin = fields.Float( 
        string='Margen'
    )
    margin_percent = fields.Float( 
        string='Margen %'
    )
    
    @api.one
    def action_calculate_margin_percent(self):
        self.margin_percent = 0                    
        if self.margin!=0 and self.amount_untaxed>0:
            margin_percent = (self.margin / self.amount_untaxed) * 100
            self.margin_percent = "{:.2f}".format(margin_percent)

    @api.one
    def action_invoice_open(self):
        self.action_regenerate_margin()
        return super(AccountInvoice, self).action_invoice_open()
    
    @api.multi    
    def action_regenerate_margin_multi(self):
        for item in self:
            item.action_regenerate_margin()    
    
    @api.one    
    def action_regenerate_margin(self):
        if self.type in ['out_invoice', 'out_refund']:
            if self.state in ['open', 'paid']:
                if self.invoice_line_ids!=False:
                    margin = 0
                    #operations                    
                    if self.type=='out_invoice':                    
                        for invoice_line_id in self.invoice_line_ids:
                            margin_line = 0
                            #invoice_line_id
                            if invoice_line_id.sale_line_ids!=False:
                                for sale_line_id in invoice_line_id.sale_line_ids:
                                    margin_line += sale_line_id.margin
                            else:
                                if self.invoice_line_id.product_id.id>0:
                                    margin_line = invoice_line_id.price_subtotal - (self.invoice_line_id.product_id.standar_price * invoice_line_id.quantity)
                            #margin_line
                            invoice_line_id.margin = "{:.2f}".format(margin_line)
                            #action_calculate_margin_percent
                            invoice_line_id.action_calculate_margin_percent()                            
                            #margin
                            margin += margin_line
                    else:#out_refund
                        if self.origin!=False:                            
                            account_invoice_ids = self.env['account.invoice'].search([('number', '=', self.origin)])
                            if len(account_invoice_ids)>0:
                                origin_invoice_id = account_invoice_ids[0]
                                #invoice_line_ids
                                for invoice_line_id in self.invoice_line_ids:
                                    margin_line = 0
                                    #search in origin invoice
                                    for origin_invoice_line_id in origin_invoice_id.invoice_line_ids:
                                        if origin_invoice_line_id.product_id.id==invoice_line_id.product_id.id:
                                            #buscamos el coste del PV del que viene
                                            purchase_price_line = 0                                            
                                            for sale_line_id in origin_invoice_line_id.sale_line_ids:
                                                purchase_price_line = sale_line_id.purchase_price
                                            #calculamos el margen de esta linea
                                            margin_line = invoice_line_id.price_subtotal - (purchase_price_line * invoice_line_id.quantity)
                                    #margin_line
                                    invoice_line_id.margin = "{:.2f}".format(margin_line)
                                    #action_calculate_margin_percent
                                    invoice_line_id.action_calculate_margin_percent()
                                    #margin
                                    margin += margin_line                                                                                               
                    #margin                                            
                    self.margin = "{:.2f}".format(margin)
                    #action_calculate_margin_percent
                    self.action_calculate_margin_percent()                    