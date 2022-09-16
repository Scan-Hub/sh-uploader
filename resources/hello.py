# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from flask_restful import Resource

from models import UserModel
from connect import security


class HelloWorld(Resource):

    @security.http(
        # login_required=True
    )
    def get(self):
        UserModel.find({
        }, cache=True)
        return {'hello': 'world'}

    @security.http(
       
        login_required=True 
    )
    def post(self, form_data, params, user):
        UserModel.find({
            **form_data
        }, cache=True)
        return {}
