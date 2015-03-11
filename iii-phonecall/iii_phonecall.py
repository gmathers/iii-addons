# -*- coding: utf-8 -*-

from openerp import models, fields, api

class crm_phonecall(models.Model):
    _inherit = 'crm.phonecall'

    repair_id = fields.Many2one(comodel_name="mrp.repair", string="Repair", required=False, )

class mrp_repair(models.Model):
    _inherit = 'mrp.repair'

    phonecalls = fields.One2many(comodel_name="crm.phonecall", inverse_name="repair_id", string="Phonecalls", required=False, )
