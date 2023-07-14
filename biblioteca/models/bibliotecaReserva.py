# -*- coding: utf-8 -*-
'''
Created on 6 jul 2023

@author: jesus.plaza
'''

from odoo import api, fields, models, _
from datetime import datetime, timedelta



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
    notes= fields.Text('Notes') 

    
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
    
    
    @api.model                
    def create(self, vals):
        if 'start_date' in vals:
            vals['end_date'] = self._calculaFechaFin(vals['start_date'])
        return super(bibliotecaReserva, self).create(vals)
    
    
    def write(self, vals):
        if 'start_date' in vals:
            vals['end_date'] = self._calculaFechaFin(vals['start_date'])
        return super(bibliotecaReserva, self).write(vals)
    
    
    def _calculaFechaFin(self,start_date):
        fecha = fields.Date.from_string(start_date)
        fecha_fin = fecha + timedelta(days=3)  
        return fecha_fin.strftime("%Y-%m-%d")
    
    
    num_employee = fields.Integer('Employees', compute='_get_num_employees')
    

    def view_all_employees(self):
        self.ensure_one()
        ids = self.env['biblioteca.reserva'].read_group([ ("book_id", "=", self.book_id.id)], fields=['employee_id'], groupby=['employee_id'])
        list = []
        for id in ids:
            list.append(id['employee_id'][0])
            
        return {
            'type': 'ir.actions.act_window',
            'name': 'Employees',
            'view_mode': 'tree',
            'res_model': 'hr.employee',
            'domain': [('id', 'in', list)],
        }
        
    def _get_num_employees(self):
        ids = self.env['biblioteca.reserva'].read_group([ ("book_id", "=", self.book_id.id)], fields=['employee_id'], groupby=['employee_id'])
        self.num_employee = len(ids) or 0
        
    
    
    num_book = fields.Integer('Books', compute='_get_num_employee_books')
    
    def view_all_books_employee(self):
        self.ensure_one()
        ids = self.env['biblioteca.reserva'].read_group([ ("employee_id", "=", self.employee_id.id)], fields=['book_id'], groupby=['book_id'])
        list = []
        for id in ids:
            list.append(id['book_id'][0])
        return {
            'type': 'ir.actions.act_window',
            'name': 'Employee books',
            'view_mode': 'tree',
            'res_model': 'biblioteca.libro',
            'domain': [('id', 'in', list)],
        }
        
    def _get_num_employee_books(self):
        ids = self.env['biblioteca.reserva'].read_group([ ("employee_id", "=", self.employee_id.id)], fields=['book_id'], groupby=['book_id'])
        self.num_book = len(ids) or 0
    
    
    