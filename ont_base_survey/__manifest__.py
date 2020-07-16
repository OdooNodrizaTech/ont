# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Ont Base Survey",
    "version": "12.0.1.0.0",
    "author": "Odoo Nodriza Tech (ONT)",
    "website": "https://nodrizatech.com/",
    "category": "Tools",
    "license": "AGPL-3",
    "depends": [
        "base",
        "sale",
        "survey",
        "survey_extra"
    ],
    "data": [
        "views/survey_user_input_view.xml",
        "views/survey_result_matrix.xml",
    ],        
    "installable": True
}