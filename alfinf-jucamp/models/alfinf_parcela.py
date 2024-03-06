# Copyright 2024 Pablo Martín - Alfinf
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

import string
from odoo import fields, models

class AlfinfParcela(models.Model):
    _inherit = 'alfinf.parcela'

    nombre = fields.Char(
        string='Parcela',
    )
    recinto = fields.Integer(
        string='Recinto'
    )
    sector = fields.Char(
        string='Sector',
    )
    poligono = fields.Char(
        string='Poligono',
        required=True,
    )
    trace_id = fields.Many2one(
        string='Trazabilidad',
        comodel_name='alfinf.traza',
        inverse_name='parcela_id',
    )
    trazacoste_id = fields.Many2one(
        string='Trazacoste',
        comodel_name='alfinf.trazacoste',
        inverse_name='parcela_id',
    )
    trazanomina_id = fields.Many2one(
        string='Trazanomina',
        comodel_name='alfinf.tracenomina',
        inverse_name='parcela_id',
    )
    variedad_id = fields.Many2one(
        string='Variedad',
        comodel_name='alfinf.variedad',
        inverse_name='parcela_id',
    )
    municipio_id = fields.Many2one(
        string='ciudad',
        comodel_name='res.city'
    )
