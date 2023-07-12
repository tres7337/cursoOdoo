# -*- coding: utf-8 -*-
'''
Created on 12 jul 2023

@author: jesus.plaza
'''

from odoo import api, fields, models, _


class bibliotecaReview(models.Model):
    """ Modelo review de la biblioteca """
    _name = "biblioteca.review"
    _description = "Review de un libro"
    _order = "rating desc"
    
    def _empleadoPorDefecto(self):
            return self.env.user.employee_ids[0].id
    
    employee_id = fields.Many2one('hr.employee','Employee', default=_empleadoPorDefecto)
    book_id = fields.Many2one('biblioteca.libro','Book', required=True)
    name = fields.Char('Name',compute='_calculaNombre', store=True)
    text = fields.Html('Text review')
    rating = fields.Selection ([('0','Sin review'),
                                ('1','Muy mala'),
                                ('2','Mala'),
                                ('3','Mediocre'),
                                ('4','Buena'),
                                ('5','Muy buena')])

    @api.depends('employee_id','book_id')
    def _calculaNombre(self):
        for record in self:
            value = ''
            if record.employee_id and record.employee_id.name:
                value += record.employee_id.name
            value +=','
            if record.book_id and record.book_id.name:
                value += record.book_id.name
            record.name = value