# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from resources.secure.video import SecureVideoUploadResource
from resources.secure.image import SecureImageUploadResource

secure_resources = {
        '/video': SecureVideoUploadResource,
        '/image': SecureImageUploadResource,
}