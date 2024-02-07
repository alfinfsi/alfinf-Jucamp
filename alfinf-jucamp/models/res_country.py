# Copyright 2024 Pablo Martín - Alfinf
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

import string
from odoo import fields, models

class ResCountry(models.Model):
    _inherit = 'res.country'


    factura_ids= fields.One2many(
        string='Facturas',
        comodel_name='alfinf.factura',
        inverse_name='pais_id',
    )

