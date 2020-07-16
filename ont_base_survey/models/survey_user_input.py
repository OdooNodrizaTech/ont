# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class SurveyUserinput(models.Model):
    _inherit = 'survey.user_input'

    call_tried = fields.Integer(        
        string='Nº intentos'
    )
    date_next_tried = fields.Datetime(        
        string='Fecha siguiente intentos'
    )