



from config import Config
import traceback
import requests
from datetime import datetime
from lib.logger import logger
from helper.uploader import UploaderService
from models import UploaderModel
 
def get_status_video_interval():
    
    # Get list video not process 100% yet
    _filter = {
        "type": "video",
        "status": "init"
    }
    _videos = UploaderModel.find(filter=_filter)
    
    for video in _videos:
        # # step 4, GET your Video to check it's progress
        url_request = f"{Config.URL_UPLOAD_VIDEO}/video/{video.get('video_id')}"
        method = "GET"
        try:
            headers = {
                'Content-Type': 'application/json',
                'x-tva-sa-id': Config.API_KEY,
                'x-tva-sa-secret': Config.SECRET_KEY
            }
            _response = requests.request(method=method, 
                                    url=url_request,
                                    headers=headers)
         
            logger.debug(_response)
            
            _item = _response.json().get("body").get("videos")[0]
            # only update path video on success process
            if _item.get("state") == 'success':
                _update = {
                    "status": _item.get("state"),
                    "path": _item.get("source_uri"),
                    "metadata": {
                        "duration": _item.get("duration"),
                        "resolution": _item.get("resolution"),
                        "playback_uri":_item.get("playback_uri"),
                        "create_time": _item.get("create_time"),
                        "update_time": _item.get("update_time"),
                    }
                }
                UploaderModel.update_one(
                    filter={
                        "video_id": video.get("video_id")
                        },
                    obj=_update, upset=True)
                
                logger.debug(_update)
                
        except Exception as e:
            traceback.print_exc(e)
                            
    
