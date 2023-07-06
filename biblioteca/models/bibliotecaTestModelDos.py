# -*- coding: utf-8 -*-


from odoo import api, fields, models, _


class bibliotecaTestModelDos(models.Model):
    """ Modelo con todos los campos del sistema para ver el funcionamiento de cada uno """
    _name = "biblioteca.test.model.dos"
    _description = "Ejemplo de campos"
    _order = "name desc"
    
    name = fields.Char('Field Short Text')
    f_many2one = fields.Many2one('biblioteca.test.model', string="Many2one")