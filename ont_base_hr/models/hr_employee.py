# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    academic_training = fields.Text(
        string='Academic training'
    )
    additional_courses = fields.Text(
        string='Additional courses'
    )
    professional_skills = fields.Text(
        string='Profesisonal skills'
    )
    professional_goals = fields.Text(
        string='Professional Goals'
    )
    personal_skills = fields.Text(
        string='Personal Skills'
    )
