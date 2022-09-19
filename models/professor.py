# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SchoolProfessor(models.Model):
    _name = 'school.professor'

    f_name = fields.Char('First name')
    l_name = fields.Char('Last name')
    sexe = fields.Selection([('male','Male'),('female','Female')])
    identity_card = fields.Char('Identity Card')
    adresse = fields.Text()
    birthday = fields.Date('Birthday')
    start_date=fields.Datetime('Start Date')
    email=fields.Char()
    phone=fields.Char()
    desc=fields.Html("type here")

    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100
