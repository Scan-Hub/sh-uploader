# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""


ALLOWED_EXTENSIONS = {'mp4', 'webm'}
ALLOWED_EXTENSIONS_IMAGE = {'jpg', 'jpeg', 'png', 'webp'}

def allowed_file(filename, regex):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in regex


def allowed_file_video(filename):
        return allowed_file(filename, ALLOWED_EXTENSIONS)


def allowed_file_image(filename):
        return allowed_file(filename, ALLOWED_EXTENSIONS_IMAGE)
