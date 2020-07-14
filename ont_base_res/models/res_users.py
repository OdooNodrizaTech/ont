# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models, fields


class ResUsers(models.Model):
    _inherit = 'res.users'
    
    commercial_phone = fields.Char( 
        string='Commercial phone'
    )
    commercial_email = fields.Char( 
        string='Commecial email'
    )