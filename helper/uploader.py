# -*- coding: utf-8 -*-

from config import Config
import traceback
import requests
import boto3, botocore
from werkzeug.utils import secure_filename
from datetime import datetime
from botocore.client import ClientError
from lib.logger import logger
from exception import NotUploadToS3Success


class UploaderService(object):
    
    @staticmethod
    def upload_video_service(file = None):
        
        url_request = f"{Config.URL_UPLOAD_VIDEO}/upload"
        method = "POST"
        try:
          
            headers = {
                'Content-Type': 'application/octet-stream',
                'x-tva-sa-id': Config.API_KEY,
                'x-tva-sa-secret': Config.SECRET_KEY
            }
            response = requests.request(method=method, 
                                    url=url_request,
                                    data= file,
                                    headers=headers)
            
            logger.debug("UPLOAD-VIDEO")
            logger.debug(response.json())
            
            #execute transcode video
            logger.debug("TRANSCODE-VIDEO")
            _resource_id = response.json().get("body").get("uploads")[0].get("id")
            _video = execute_transcode(_resource_id)
            logger.debug(_video)

            return _video
            
        except Exception as e:
            logger.debug(e)

        return None

    @staticmethod
    def upload_to_s3(file, _is_secure=False):
        if not file:
            return None
        file.filename = secure_filename(file.filename)
        _bucket_name = Config.S3_BUCKET
        if _is_secure:
            _bucket_name = Config.S3_BUCKET_INTERNAL
        print("_bucket_name ", _bucket_name)
        output = upload_file_to_s3(file, _bucket_name, _is_secure)
        if not output:
            raise NotUploadToS3Success
        return str(output)


def execute_transcode(source_upload_id: str()):
    logger.debug(source_upload_id)
    # step 3, Transcode a Video using an Upload
    _data = {
            "source_upload_id": source_upload_id,
            "playback_policy": 'public'
    }
    
    url_request = f"{Config.URL_UPLOAD_VIDEO}/video"
    method = "POST"
    try:
        headers = {
            'x-tva-sa-id': Config.API_KEY,
            'x-tva-sa-secret': Config.SECRET_KEY
        }
        print("REQUEST-TRANSCODE ", data, url_request, method, headers)

        response = requests.request(method=method, 
                                url=url_request,
                                data= _data,
                                headers=headers)
        print("RESPONSE-TRANSCODE ", response)
        logger.debug(response.json())
        return response.json().get("body").get("videos")[0]
    
    except Exception as e:
       logger.debug(e)

    
def upload_file_to_s3(file, bucket_name, is_internal=False):
    """
    Docs: http://boto3.readthedocs.io/en/latest/guide/s3.html
    """
    try:
        _access_key = Config.S3_KEY
        _access_key_secret = Config.S3_SECRET

        if is_internal:
            
            _access_key = Config.S3_KEY_INTERNAL
            _access_key_secret = Config.S3_SECRET_INTERNAL


        s3 = boto3.client(
        "s3",
        endpoint_url=Config.S3_HOST,
        aws_access_key_id=_access_key,
        aws_secret_access_key=_access_key_secret,
        use_ssl=False,
        )
        cur_date =  datetime.today().strftime('%Y/%m/%d')
        name_prefix =  datetime.today().strftime('%hh%MM%ss')

        key_path_upload = f'scanhub/{cur_date}/{name_prefix}_{file.filename}'
        logger.debug(key_path_upload)
        s3.upload_fileobj(
            file,
            bucket_name,
            key_path_upload,
            ExtraArgs={
                "ContentType": file.content_type    #Set appropriate content type as per the file
            }
        )
    except Exception as e:
        logger.debug(e)
        return None
    return f'{Config.S3_HOST}/{bucket_name}/{key_path_upload}'
   