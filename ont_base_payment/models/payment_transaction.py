# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging
from odoo import models, api

_logger = logging.getLogger(__name__)


class PaymentTransaction(models.Model):
    _inherit = 'payment.transaction'

    @api.model
    def action_payment_transaction_done_error(self, error):
        _logger.info(error)
