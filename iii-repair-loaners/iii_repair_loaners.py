# -*- coding: utf-8 -*-

from openerp import models, fields, api

AVAILABLE_CONDITIONS = [
    ('0', 'Very Poor'),
    ('1', 'Poor'),
    ('2', 'Good'),
    ('3', 'Very Good'),
    ('4', 'Excellent'),
]

AVAILABLE_COURIERS = [
    ('0', 'Purolator'),
    ('1', 'Bus'),
    ('2', 'Other'),
    ]

class Loaner(models.Model):
    _name = 'loaners.loaner'
    _description = 'Loaner'

    type = fields.Selection(string="Type", selection=[('0', 'Autoclave'), ('1', 'Centrifuge'), ('2', 'Other'), ], required=True, )
    other_type = fields.Char(string="Other Type", required=False, )
    brand = fields.Char(string="Brand", required=True, )
    name = fields.Char(string="Model", required=True, )
    serial_number = fields.Char(string="Serial Number", required=True, )
    date_manufactured = fields.Date(string="Date Manufactured", required=False, default=fields.Date.today, )
    condition = fields.Selection(string="Condition", selection=AVAILABLE_CONDITIONS, required=False, )
    notes = fields.Text(string="Notes", required=False, )
    active = fields.Boolean(default=True)
    usages = fields.One2many(comodel_name="loaners.loaner_usage", inverse_name="loaner_used", string="Usages", required=False, )
    display_name = fields.Char(compute='_compute_display_name')

    @api.one
    @api.depends('brand', 'name', 'serial_number')
    def _compute_display_name(self):
        b = " "
        n = " "
        s = " "
        if self.brand:
            b = self.brand
        if self.name:
            n = self.name
        if self.serial_number:
            s = " s/n " + self.serial_number
        self.display_name = b + " " + n + s

    def name_get(self, cr, uid, ids, context=None):
        result = {}
        for loaner in self.browse(cr, uid, ids, context=context):

            result[loaner.id] = loaner.brand + " " + loaner.name + " " + loaner.serial_number

        return result.items()

class Loaner_Usage(models.Model):
    _name = 'loaners.loaner_usage'
    _description = 'Loaner Usage'

    loaner_used = fields.Many2one(comodel_name="loaners.loaner", string="Loaner Used", required=False, )
    cord = fields.Boolean(string="Cord", )
    rack = fields.Boolean(string="Rack", )
    trays = fields.Selection(string="Trays", selection=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ], required=False, )
    accessories = fields.Char(string="Other Accessories", required=False, )
    date_out = fields.Date(string="Date Loaner Sent", required=False, )
    shipping_out_paid = fields.Boolean(string="Shipping Out Paid by us",  )
    courier_out = fields.Selection(string="Outbound Courier", selection=AVAILABLE_COURIERS, required=False, )
    courier_out_other = fields.Char(string="Other Outbound Courier", required=False, )
    tracking_out = fields.Char(string="Outbound Tracking #", required=False, )
    amount_out = fields.Float(string="Outbound Shipping Cost",  required=False, )
    condition_out = fields.Selection(string="Condition When Sent", selection=AVAILABLE_CONDITIONS, required=False, )
    date_back = fields.Date(string="Date Loaner Returned", required=False, )
    shipping_back_paid = fields.Boolean(string="Shipping Back Paid by us",  )
    courier_back = fields.Selection(string="Return Courier", selection=AVAILABLE_COURIERS, required=False, )
    courier_back_other = fields.Char(string="Other Return Courier", required=False, )
    tracking_back = fields.Char(string="Return Tracking #", required=False, )
    amount_back = fields.Float(string="Return Shipping Cost",  required=False, )
    condition_back = fields.Selection(string="Condition When Returned", selection=AVAILABLE_CONDITIONS, required=False, )
    state = fields.Selection(string="State", selection=[('0', 'On Loan'), ('1', 'QC Testing'), ('2', 'Done'), ], required=False, )
    notes = fields.Text(string="Notes", required=False, )

