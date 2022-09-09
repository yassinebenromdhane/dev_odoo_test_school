# -*- coding: utf-8 -*-
import json
from datetime import datetime
from odoo import http
from odoo.http import request, Response

class School(http.Controller):
    @http.route('/school/school', auth='public',type='http',csrf=False,methods=['POST'])
    def index(self, **kw):
        students_rec =request.env['school.student'].search([])
        students=[]
        for rec in students_rec:
            # birthday = datetime.strptime(rec.birthday, '%Y-%m-%d').date()
            # print("student id :",type(birthday))
            val={
                'id':rec.id,
                'f_name':rec['f_name'],
                'l_name':rec['l_name'],
                'sexe':rec['sexe'],
                'identity_card':rec['identity_card'],
                'email':rec['email']
            }
            students.append(val)

        data={
            'status':'200',
            'message':'success',
            'students':students        
        }
        data_json=json.dumps(data)
        return data_json
        # return Response(json.dumps(body), headers=headers)
    def action_test(self):
        print("clicked me!!")
    # @http.route('/school/school/students', auth='public')
    # def list(self, **kw):
    #     students =http.request.env['school.student'].search([])
    #     return students
        
#     @http.route('/school/school/objects/<model("school.school"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('school.object', {
#             'object': obj
#         })
