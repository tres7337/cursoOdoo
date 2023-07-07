# -*- coding: utf-8 -*-
'''
Created on 6 jul 2023

@author: jesus.plaza
'''

from odoo import api, fields, models, _


class bibliotecaLibro(models.Model):
    """ Modelo libro de la biblioteca """
    _name = "biblioteca.libro"
    _description = "Libro de una biblioteca"
    _order = "name desc"
    
    
    name = fields.Char('Nombre')