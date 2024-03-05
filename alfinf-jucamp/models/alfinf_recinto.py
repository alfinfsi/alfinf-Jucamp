# Copyright 2024 Pablo Martín - Alfinf
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

import string
from odoo import fields, models

class AlfinfRecinto(models.Model):
    _name = 'alfinf.recinto'

    nombre = fields.Char(
        string='Nombre'
    )

    parcela_id = fields.Many2one(
        string='Parcela',
        comodel_name='alfinf.parcela',
        inverse_name='recinto_ids'
    )
    trace_ids = fields.One2many(
        string='Trazas commerce',
        comodel_name='alfinf.trace',
        inverse_name='recinto_id'
    )
    tracenomina_ids = fields.One2many(
        string='Trazas de nominas',
        comodel_name='alfinf.tracenomina',
        inverse_name='recinto_id'
    )
    tracecoste_ids = fields.One2many(
        string='Trazas de coste',
        comodel_name='alfinf.tracecoste',
        inverse_name='recinto_id'
    )
    variedad_id = fields.Many2one(
        string='Variedad',
        comodel_name='alfinf.variedad',
        inverse_name='recinto_ids'
    )
