# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields


class AccountAccount(models.Model):
    _inherit = 'account.account'

    custom_type = fields.Selection(
        [
            ('fixed', 'Fijo'),
            ('variable', 'Variable')
        ],
        string='Tipo (fijo o variable)'
    )
    custom_classification = fields.Selection(
        [
            ('personal', 'Personal'),
            ('structural', 'Estructural'),
            ('marketing', 'Marketing'),
            ('amortization', 'Amortizacion'),
            ('minority:investment', 'Inversion minoritaria'),
            ('transportation', 'Transporte'),
            ('financial', 'Financiero'),
            ('other', 'Otro'),
        ],
        string='Clasificacion'
    )
