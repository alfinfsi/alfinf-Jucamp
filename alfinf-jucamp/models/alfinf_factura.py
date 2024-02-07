# Copyright 2024 Pablo Martín - Alfinf
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

import string
from odoo import fields, models


class AlfinfFactura(models.Model):
    _name = 'alfinf.factura'
    _description = 'Facturas de a3ERP'
    _rec_name = 'num_Factura'
    
    num_Factura = fields.Char(
        string="Numero de factura"
    )
    fecha_Factura = fields.Date(
        string="Fecha de factura"
    )
    scta_Cliente = fields.Char(
        string="Cuenta de cliente"
    )
    cliente = fields.Integer(
        string="Cliente"
    )
    euBase = fields.Char(
        string="Base"
    )
    pc_IVA = fields.Integer(
        string="Porcentaje de IVA"
    )
    scta_IVA = fields.Float(
        string="Cuenta de IVA",
        digits=(12, 2)
    )
    euIVA = fields.Char(
        string="IVA"
    )
    stca_Venta = fields.Char(
        string="Cuenta de venta"
    )
    euTotal = fields.Float(
        string="Total",
        digits=(12, 2)
    )
    fecha_Operacion = fields.Date(
        string="Fecha de operacion"
    )
    r_Fecha_Factura = fields.Char(
        
    )
    r_Num_Factura = fields.Char(
        
    )
    r_euBase = fields.Char(
        
    )
    r_euIVA = fields.Char(
        
    )
    tipo_Rectificativa = fields.Char(
        string="tipo rectificativa"
    )
    pais_id = fields.Many2one(
        string="Pais",
        comodel_name="res.country",
        inverse_name="factura_ids"
    )