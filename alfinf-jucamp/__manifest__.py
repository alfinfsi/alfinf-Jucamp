# Copyright 2024 Pablo Martín - Alfinf
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "Alfinf Jucamp",
    "summary": "Alfinf Jucamp",
    "version": "16.0.1.0.0",
    "development_status": "Beta",
    "license": "AGPL-3",
    "author": "Alfinf",
    "website": "https://github.com/alfinfsi/",
    "category": "Connector",
    "depends": [
        "sale",
        "sale_management",
        "contacts",
        "l10n_es_toponyms"
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/alfinf_trace_view.xml",
        "views/alfinf_tracenomina_view.xml",
        "views/alfinf_tracecoste_view.xml",
        "views/alfinf_parcela_view.xml",
        "views/alfinf_finca_view.xml",
        "views/alfinf_marca_view.xml",
        "views/alfinf_vivero_view.xml",
    ],
    "installable": True,
}
