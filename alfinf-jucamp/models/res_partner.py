# Copyright 2024 Manuel Calero - Alfinf
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    alfinf_trace_ids = fields.One2many(
        string='Traza',
        comodel_name='alfinf.trace',
        inverse_name='res_partner_id'
    )
    alfinf_tracenomina_ids = fields.One2many(
        string='Trazas nomina',
        comodel_name='alfinf.tracenomina',
        inverse_name='res_partner_id'
    )
    alfinf_tracecoste_ids = fields.One2many(
        string='Trazas coste',
        comodel_name='alfinf.tracecoste',
        inverse_name='res_partner_id'
    )
