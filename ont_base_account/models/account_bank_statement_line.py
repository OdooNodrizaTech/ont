# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models


class AccountBankStatementLine(models.Model):
    _inherit = 'account.bank.statement.line'

    @api.multi
    def get_move_lines_for_reconciliation_widget(self,
                                                 excluded_ids=None,
                                                 str=False,
                                                 offset=0,
                                                 limit=None
                                                 ):
        res = super(AccountBankStatementLine, self).\
            get_move_lines_for_reconciliation_widget(
                excluded_ids,
                str,
                offset,
                limit
            )
        # operations (reverse)
        if res:
            res = list(reversed(res))
        # return
        return res
