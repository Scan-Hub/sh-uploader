# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from resources.health_check import HealthCheck
from resources.iapi import iapi_resources
from resources.secure import secure_resources

api_resources = {
    '/common/health_check': HealthCheck,
    **{f'/iapi{k}': val for k, val in iapi_resources.items()},
    **{f'/secure{k}': val for k, val in secure_resources.items()}

}
