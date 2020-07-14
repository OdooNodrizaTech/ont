# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from openerp import api, models, fields

class HrEmployee(models.Model):
    _inherit = 'hr.employee'
    
    academic_training = fields.Text( 
        string='Formacion academica',
    )
    additional_courses = fields.Text( 
        string='Cursos adicionales',
    )
    professional_skills = fields.Text( 
        string='Habilidades profesionales',
    )
    professional_goals = fields.Text( 
        string='Metas profesionales',
    )
    personal_skills = fields.Text( 
        string='Habilidades personales',
    )