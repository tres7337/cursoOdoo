# -*- coding: utf-8 -*-

def migrate(cr, version):
    value = 'Notas insertadas por la migración'
    cr.execute('UPDATE biblioteca_reserva SET notes=%s where notes is null',[value])