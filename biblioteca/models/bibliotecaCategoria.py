# -*- coding: utf-8 -*-
'''
Created on 6 jul 2023

@author: jesus.plaza
'''

from odoo import api, fields, models, _


class bibliotecaCategoria(models.Model):
    """ Modelo categoria de un libro"""
    _name = "biblioteca.categoria"
    _description = "Categoria de un libro"
    _order = "name desc"
    
    
    name = fields.Char('Nombre')