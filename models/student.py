# -*- coding: utf-8 -*-
from datetime import date
from email import message
from email.policy import default
from odoo import models, fields, api
# from addons.base_rest import restapi
# from addons.component.core import Component
# from addons.base_rest.controllers import main

class SchoolStudent(models.Model):
    _name = 'school.student'
    _description='students of the school for exmpl'
    _inherit =  ['mail.thread','mail.activity.mixin']
   
    f_name = fields.Char('First name')
    l_name = fields.Char('Last name')
    sexe = fields.Selection([('male','Male'),('female','Female')])
    identity_card = fields.Char('Identity Card')
    adresse = fields.Text()
    birthday = fields.Date('Birthday')
    age=fields.Integer(string='age')
    # image=fields.Binary()
    registration_date=fields.Datetime('Registration Date',default=fields.Datetime.now)
    email=fields.Char()
    phone=fields.Char()
    classroom_id=fields.Many2one(comodel_name="school.classroom" , string="Classroom")
    code=fields.Char(string='Code Class')
    priority=fields.Selection([
        ('0','Normale'),
        ('1','Low'),
        ('2','High'),
        ('3','Very High'),
        ('4','Expert')
    ],string="Priority")
    state=fields.Selection([
        ('draft','Draft'),
        ('in_consultation','In Consultation'),
        ('done','Done'),
        ('cancel','Cancelled'),
    ],string="Statues",default="draft")
    

    @api.depends("birthday")
    def _computed_age(self):
        for rec in self:
            today=date.today()   
            if rec.birthday:
                rec.age=today.year-rec.birthday.year
                print('rec.age',rec.age)
            else:
                rec.age =0

                
    def action_test(self):
        print("Button clicked")
        return {
            'effect':{
                'fadeout':'slow',
                'message':'Click Succefull',
                'type':'rainbow_man'
            }
        }

    # !  action button else not working !!! 
    # @api.onchange('classroom_id')
    # def onchange_code(self):
    #     self.code=self.classroom_id.code 

        
    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100
