# -*- coding: utf-8 -*-
from odoo import api, models, fields, _
from odoo.exceptions import ValidationError


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = "mail.thread"
    _description = 'Patient Records'

    name = fields.Char(string="name", required= True, tracking=True)
    age = fields.Integer(string="Age", tracking=True)
    is_child = fields.Boolean(string="Is Child ?", tracking=True)
    notes = fields.Text(string="Notes")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')], string="Gender", tracking=True)
    capitalized_name = fields.Char(string="Capitalized name", compute= '_compute_capitalized_name')
    ref = fields.Char(string="Reference", default=lambda self: _('New'))
    doctor_id = fields.Many2one('hospital.doctor', string="Doctor",)
    active = fields.Boolean(default=True)
    
    tag_ids = fields.Many2many('res.partner.category', 'hospital_patient_tag_rel', 'patient_id', 'tag_id' ,string="Tags")

    @api.model_create_multi
    def create(self, value_list):
        for vals in value_list:
            vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient') or _('New')
            return super(HospitalPatient, self).create(value_list)
    @api.constrains('is_child', 'age')
    def check_child_age(self):
        for rec in self:
            if rec.is_child and rec.age == 0:
                raise ValidationError(_("Age has to be recorded"))

    @api.depends('name')
    def _compute_capitalized_name(self):
        for rec in self:
            if rec.name:
                rec.capitalized_name = rec.name.upper()
            else:
                rec.capitalized_name = ''



    @api.onchange('age')
    def _onchange_age(self):
        if self.age <= 10:
            self.is_child = True
        else:
            self.is_child =False