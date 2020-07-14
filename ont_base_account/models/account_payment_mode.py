# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
import logging
_logger = logging.getLogger(__name__)

from openerp import api, models, fields
from openerp.exceptions import Warning

class AccountPaymentMode(models.Model):
    _inherit = 'account.payment.mode'
    _order = 'position'
    
    position = fields.Integer(
        string='Posicion'
    )
    show_payment_method_id_journal_ids_in_pdf = fields.Boolean(
        string='Mostrar en PDF',
        help='Mostrar los numeros de cuenta de el/los diario/s del metodo de pago vinculado en los PDFs (Presupuesto y Factura)',
        default=False
    )