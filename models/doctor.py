# -*- coding: utf-8 -*-
from odoo import api, models, fields, _
from odoo.exceptions import ValidationError


class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _inherit = "mail.thread"
    _description = 'Doctor Records'
    _rec_name = 'ref'
    name = fields.Char(string="name", required= True, tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')], string="Gender", tracking=True)
    ref = fields.Char(string="Reference", default=lambda self: _('New'))
    active = fields.Boolean(default=True)


    @api.model_create_multi
    def create(self, value_list):
        for vals in value_list:
            vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.doctor') or _('New')
            return super(HospitalDoctor, self).create(value_list)



    def name_get(self):
        res = [];
        for rec in self:
            name = f'{rec.ref} - ({rec.name})'
            res.append((rec.id, name))
        return res