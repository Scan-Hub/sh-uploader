# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from lib import DaoModel, AsyncDaoModel
from connect import connect_db, redis_cluster, asyncio_mongo

UserModel = DaoModel(connect_db.db.users, redis=redis_cluster)
AsyncUserModel = AsyncDaoModel(asyncio_mongo.db.users)

UploaderModel = DaoModel(connect_db.db.uploader)