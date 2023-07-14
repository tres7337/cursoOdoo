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
            
            
    num_employee = fields.Integer('Employees', compute='_get_num_employees')
    

    def view_all_employees(self):
        self.ensure_one()
        ids = self.env['biblioteca.review'].read_group([ ("book_id", "=", self.book_id.id)], fields=['employee_id'], groupby=['employee_id'])
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
        ids = self.env['biblioteca.review'].read_group([ ("book_id", "=", self.book_id.id)], fields=['employee_id'], groupby=['employee_id'])
        self.num_employee = len(ids) or 0
    