# -*- coding: utf-8 -*-
'''
Created on 5 jul 2023

@author: jesus.plaza
'''

from odoo import api, fields, models, _


class bibliotecaTestModel(models.Model):
    """ Modelo con todos los campos del sistema para ver el funcionamiento de cada uno """
    _name = "biblioteca.test.model"
    _description = "Ejemplo de campos"
    _order = "f_char desc"

    