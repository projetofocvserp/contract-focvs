# Copyright 2004-2010 OpenERP SA
# Copyright 2014-2018 Tecnativa - Pedro M. Baeza
# Copyright 2015 Domatix
# Copyright 2016-2018 Tecnativa - Carlos Dauden
# Copyright 2017 Tecnativa - Vicent Cubells
# Copyright 2016-2017 LasLabs Inc.
# Copyright 2018-2019 ACSONE SA/NV
# Copyright 2020-2021 Tecnativa - Pedro M. Baeza
# Copyright 2020 Tecnativa - Víctor Martínez
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Recurring - Contracts Management",
    "version": "14.0.1.1.0",
    "category": "Contract Management",
    "license": "AGPL-3",
    "author": "Tecnativa, ACSONE SA/NV, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/contract",
    "depends": ["base", "product", "portal", "purchase"],
    "external_dependencies": {"python": ["dateutil"]},
    "data": [
        "security/ir.model.access.csv",
        "security/groups.xml",
        "security/contract_tag.xml",
        "security/contract_security.xml",
        "security/contract_terminate_reason.xml",
        "report/report_contract.xml",
        "report/contract_views.xml",
        "data/contract_cron.xml",
        "data/contract_renew_cron.xml",
        "data/mail_template.xml",
        "data/mail_message_subtype.xml",
        "data/ir_ui_menu.xml",
        "wizards/contract_line_wizard.xml",
        "wizards/contract_manually_create_invoice.xml",
        "wizards/contract_contract_terminate.xml",
        "views/contract_tag.xml",
        "views/assets.xml",
        "views/abstract_contract_line.xml",
        "views/contract.xml",
        "views/contract_line.xml",
        "views/contract_template.xml",
        "views/contract_template_line.xml",
        "views/res_partner_view.xml",
        "views/res_config_settings.xml",
        "views/contract_terminate_reason.xml",
        "views/contract_portal_templates.xml",
        "views/reajuste_preco_item_view.xml",
        "views/reajuste_preco_view.xml",
        "views/receber_fatura_line_view.xml",
        "views/receber_fatura_view.xml",
        "views/fatura_consorcio_view.xml",
        "views/contract_contrato_consorcio.xml",
        "views/contract_contrato_consorcio_linha.xml",

    ],
    "installable": True,
    "application": True,
    "sequence": 3,
}
