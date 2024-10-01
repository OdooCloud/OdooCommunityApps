# -*- coding: utf-8 -*-
{
    'name': "Security Module",
    'summary': """
        Visibillity of modules""",
    'description': """
        Set Visibillity of modules
    """,
    'author': 'Febno Technologies',
    'company': 'Febno Technologies',
    'website': "",
    'category': 'Security',
    'version': '15.0.1.0.0',
    'depends': ['base', 'account', 'project', 'hr', 'stock', 'contacts', 'purchase', 'hr_holidays', 'calendar', 'mail','crm','sale', 'sale_management'],
    'data': [
        'security/security.xml',
        'security/account_menu_access.xml',
    ],
    'images': ['static/description/banner.png'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
}
