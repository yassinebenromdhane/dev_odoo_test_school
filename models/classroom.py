# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SchoolClassroom(models.Model):
    _name = 'school.classroom'

    name = fields.Char()
    code = fields.Char()
    # depatment_id=fields.Many2many(comodel_name="school.depatment" , string="Department")
    # code_dep=fields.Char('ode department',related="depatment_id.code")