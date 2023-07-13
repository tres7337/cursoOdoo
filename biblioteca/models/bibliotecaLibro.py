# -*- coding: utf-8 -*-
'''
Created on 6 jul 2023

@author: jesus.plaza
'''

from odoo import api, fields, models, _
from datetime import datetime
from odoo.exceptions import ValidationError


class bibliotecaLibro(models.Model):
    """ Modelo libro de la biblioteca """
    _name = "biblioteca.libro"
    _description = "Libro de una biblioteca"
    _order = "title desc"
    
    
    title = fields.Char('Title', required=True)
    author = fields.Char('Author')
    name = fields.Char('Name', compute='_calculaNombre')
      
    @api.depends('title','author')
    def _calculaNombre(self):
        for record in self:
            value = ''
            if record.title:
                value += record.title
            value +=','
            if record.author:
                value += record.author
            record.name = value
            
    year = fields.Selection (selection='_calculaYear', required=True)
    
    def _calculaYear(self):
        year = datetime.now().year + 1
        array_years = []
        
        for i in range(2016, year):
            array_years.append((str(i),str(i)))
        return array_years
    
    synopsis = fields.Html('Synopsis')
    pages = fields.Integer('Number of pages')
    editorial = fields.Char('Editorial')
    
    categ_ids = fields.Many2many(
        comodel_name="biblioteca.categoria",
        relation="biblioteca_libro_categoria_rel",
        column1="libro_id",
        column2="categoria_id",
        string="Categories"
    )
    
    book = fields.Binary('Book file', required=True)
    reviews = fields.One2many('biblioteca.review','book_id','Reviews')
    
    
    @api.constrains('title','year')
    def _compruebaLibro(self):
        for record in self:
            if record.title and record.year:
                cuentaRepes = self.env['biblioteca.libro'].search_count([('title', '=', record.title ), ('year', '=', record.year)])
                print(cuentaRepes)
                if cuentaRepes > 1:
                    raise ValidationError("Fields title and year must be different from another book registered")

    
    
    
    
    
    
