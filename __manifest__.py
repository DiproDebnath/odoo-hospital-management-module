# -*- coding: utf-8 -*-
{
    'name': "Hospital Management System",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Dipro Debnath",
    'website': "https://www.Dipro.me",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Management',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', "mail"],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/menu.xml',
        'views/patient.xml',
        'views/doctor.xml',
    ],
}
