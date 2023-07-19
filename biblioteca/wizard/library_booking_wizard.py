# -*- coding: utf-8 -*-
'''
Created on 19 jul 2023

@author: jesus.plaza
'''

from odoo import api, fields, models, _, exceptions


class LibraryBookingkWizard(models.TransientModel):
   _name = "library.booking.wizard"
   _description = "Wizard de reservas"
    
   text = fields.Char('Add notes')
   choose_state = fields.Selection ([('borrador','Borrador'),
                                     ('aprobar','Aprobar'),
                                     ('reservado','Reservado'),
                                     ('caducado','Caducado'),
                                     ('rechazado','Rechazado')], 
                                     default="borrador")
    
   def addTextToNotes(self):
       bookings = self.env['biblioteca.reserva'].search([('state','=',self.choose_state)])
       bookings.write({'notes':self.text})