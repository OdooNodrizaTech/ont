# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import api, models, _
from openerp.exceptions import Warning

class MailComposer(models.TransientModel):
    _inherit = 'mail.compose.message'
    
    @api.one
    def check_limit_size_attachments(self):
        limit_size_attachments = 1000000*10
        total_size_attachments = 0
        
        if self.attachment_ids:
            for attachment_id in self.attachment_ids:
                total_size_attachments = total_size_attachments + attachment_id.file_size
        
        if total_size_attachments>=limit_size_attachments:    
            raise Warning(_('The maximum limit of email attachments is 10MB'))
    
    @api.multi
    @api.onchange('attachment_ids','template_id')
    def onchange_attachment_ids(self):
        for model_item in self:
            model_item.check_limit_size_attachments()            