# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from flask_restful import Resource

from models import UserModel
from connect import security
from flask import g, request
from lib.logger import logger
from utils import allowed_file_video
from helper.uploader import UploaderService
from models import UploaderModel
from werkzeug.utils import secure_filename
from config import Config
from bson import ObjectId
import uuid


class VideoUploadResource(Resource):

    @security.http(
        login_required=False 
    )
    def get(self):
        _id = request.args["id"]
        _item = UploaderModel.find_one({
            "_id": ObjectId(_id)   
        })
        logger.debug(_item)
        return {
            "_id": str(_item.get("_id")),
            "path": _item.get("path"),
            "status": _item.get("status")
        }

    @security.http(
        login_required=False
    )
    def post(self):
        
        if 'file' not in request.files:
            logger.debug("NotFilePart")
        
        _file = request.files['file']
        if _file == None or not allowed_file_video(_file.filename):
            logger.debug("NotSupportFile")
        
        _uuid = str(uuid.uuid4())
        _upload = {
            "name" :  secure_filename(_file.filename),
            "type": "video",
            "status": "success",
            "created_by": "core-api" ,
            "uuid": _uuid                                    
        }
        print("Config.USE_THETA ", Config.USE_THETA)
        # if Config.USE_THETA:
        #     _video = UploaderService.upload_video_service(_file)
        #     logger.debug(_video)
        #     _upload = {
        #       **_upload,
        #         "video_id": _video.get("video_id"),
        #     }
        #     logger.debug(_upload)
        # else:
        _is_secure = False
        _path = UploaderService.upload_to_s3(_file, _is_secure)
        _upload = {
            **_upload,
            "path": _path   
        }
                
        UploaderModel.insert_one(_upload)

        return {
            "uuid": _uuid,        
            "path": _path,
            "status": _upload.get("status")
        }
