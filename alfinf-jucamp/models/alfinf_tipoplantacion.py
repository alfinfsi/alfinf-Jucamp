# Copyright 2024 Pablo Martín - Alfinf
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

import string
from odoo import fields, models

class AlfinfTipoplantacion(models.Model):
    _name='alfinf.tipoplantacion'
    _description = 'Formato de los cultivos'

    name= fields.Char(
        string='Tipo de plantacion',
    )

    parcelas_ids = fields.One2many(
        comodel_name='alfinf.parcela',
        inverse_name='tipoplantacion_id',
    )
