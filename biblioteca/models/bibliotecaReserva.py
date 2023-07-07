# -*- coding: utf-8 -*-
'''
Created on 6 jul 2023

@author: jesus.plaza
'''

from odoo import api, fields, models, _


class bibliotecaReserva(models.Model):
    """ Modelo reserva de la biblioteca """
    _name = "biblioteca.reserva"
    _description = "Reserva en la biblioteca"
    _order = "name desc"
    
    
    name = fields.Char('Nombre')