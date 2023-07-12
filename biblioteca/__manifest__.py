# -*- coding: utf-8 -*-
{
    'name': 'Biblioteca',

    'summary': 'Biblioteca Virtual',

    'description': 'Módulo de una biblioteca virtual para ir cogiendo los conceptos de Odoo paso a paso',

    'author': 'Curso Odoo',
    'contributors': [
                     "Jesús Plaza <jesus.plaza@altia.es>"
                     ],
    'website': "http://www.altia.es",
    'category': 'Altia Desarrollo',
    'version': '15.0.0.0.1',
    'installable': True,
    'application': True,
    'depends': ['base','hr'
                ],
    
    # always loaded
    'data': [   
        'security/ir.model.access.csv',                 
        'views/bibliotecaAccionesView.xml',
        'views/bibliotecaMenus.xml',
        'views/bibliotecaLibroView.xml',
        'views/bibliotecaReservaView.xml',
        'views/bibliotecaCategoriaView.xml',
        'views/bibliotecaReviewView.xml',
    ],
    'qweb': [

    ],
    # only loaded in demonstration mode
}