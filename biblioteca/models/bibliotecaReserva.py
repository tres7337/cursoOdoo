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
    _order = "start_date desc"
    
    
    name = fields.Char('Name',compute='_calculaNombre')
    
    
    def _empleadoPorDefecto(self):
            return self.env.user.employee_ids[0].id
    
    employee_id = fields.Many2one('hr.employee','Employee', default=_empleadoPorDefecto)
    category_id = fields.Many2one('biblioteca.categoria','Category')
    book_id = fields.Many2one('biblioteca.libro','Book', required=True, domain="[('categ_ids','in',category_id)]")
    start_date = fields.Date('Start date',default=fields.Date.context_today, required=True)
    end_date = fields.Date('End date', required=True)
    
    state = fields.Selection ([('borrador','Borrador'),
                               ('aprobar','Aprobar'),
                               ('reservado','Reservado'),
                               ('caducado','Caducado'),
                               ('rechazado','Rechazado')], 
                               default="borrador")
    
    
    @api.depends('book_id','employee_id')
    def _calculaNombre(self):
        for record in self:
            value = ''
            if record.employee_id and record.employee_id.name:
                value += record.employee_id.name
            value +=' - '
            if record.book_id and record.book_id.name:
                value += record.book_id.name
            record.name = value
    
    