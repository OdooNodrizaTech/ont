# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models, _
from odoo.exceptions import Warning as UserError


class MailComposer(models.TransientModel):
    _inherit = 'mail.compose.message'

    @api.multi
    def check_limit_size_attachments(self):
        self.ensure_one()
        limit_size = 1000000*10
        item_size = 0

        if self.attachment_ids:
            for attachment_id in self.attachment_ids:
                item_size = item_size + attachment_id.file_size

        if item_size >= limit_size:
            raise UserError(_('The maximum limit of email attachments is 10MB'))

    @api.multi
    @api.onchange('attachment_ids', 'template_id')
    def onchange_attachment_ids(self):
        self.ensure_one()
        self.check_limit_size_attachments()
