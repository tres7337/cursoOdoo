# -*- coding: utf-8 -*-

'''
Created on 17 jul 2023

@author: jesus.plaza
'''

from odoo import api, fields, models, _

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    book_id = fields.Many2one('biblioteca.libro')
    