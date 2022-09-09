# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SchoolClassroom(models.Model):
    _name = 'school.classroom'

    name = fields.Char()
    code = fields.Char()