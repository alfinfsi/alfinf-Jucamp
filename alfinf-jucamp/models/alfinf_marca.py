# Copyright 2024 Pablo Martín - Alfinf
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

import string
from odoo import fields, models


class AlfinfMarca(models.Model):
    _name = 'alfinf.marca'
    _description = 'Marcas de comercializacion.'

    mc_marca = fields.Char(
        string='Marca',
    )
    mc_alias = fields.Char(
        string='Alias',
    )
