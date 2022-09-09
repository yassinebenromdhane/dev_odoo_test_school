# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SchoolDepatment(models.Model):
    _name = 'school.depatment'

    name = fields.Char()
    code = fields.Char()