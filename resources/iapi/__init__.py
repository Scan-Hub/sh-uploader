# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from resources.iapi.video import VideoUploadResource
from resources.iapi.image import ImageUploadResource

iapi_resources = {
        '/video': VideoUploadResource,
        '/image': ImageUploadResource,
}