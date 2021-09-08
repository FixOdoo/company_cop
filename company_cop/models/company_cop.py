from odoo import models, api, fields


class CompanyCoP(models.Model):
    _inherit = 'res.company'

    company_cop = fields.Binary(string="Company Cop")
