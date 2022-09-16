# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from marshmallow import Schema, EXCLUDE, RAISE, fields


class VideoResponse(Schema):
    class Meta:
        unknown = RAISE

    _id = fields.Str(required=True)
    status = fields.Str(required=False, default="init")
