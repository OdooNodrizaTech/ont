# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': 'Ont Margin Sale',
    'version': '12.0.1.0.0',    
    'author': 'Odoo Nodriza Tech (ONT)',
    'website': 'https://nodrizatech.com/',
    'category': 'Tools',
    'license': 'AGPL-3',
    'depends': ['base', 'sale', 'sale_margin'],
    'data': [
        'data/ir_cron.xml',
        'views/sale_order_view.xml',
    ],
    'installable': True,
    'auto_install': False,    
}