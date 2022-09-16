# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
# from lib.decorators.http import make_response
# from lib.enums.http import StatusInt
# from src.enums.http import ErrorCode


# class NotFilePart(Exception):
#     def __init__(self, message='NotFilePart', *args: object) -> None:
#         super().__init__(*args)
#         self.response = make_response(
#             error_code=ErrorCode.ErrorFileRequire,
#             msg=message
#         ), StatusInt.Bad

#     pass

# class NotSupportFile(Exception):
#     def __init__(self, message='NotSupportFile', *args: object) -> None:
#         super().__init__(*args)
#         self.response = make_response(
#             error_code=ErrorCode.ErrorFileTypeSupport,
#             msg=message
#         ), StatusInt.Bad

#     pass


class NotUploadToS3Success(Exception):
        def __init__(self, msg='Not Available for upload/Download to S3.', *args: object, **kwargs) -> None:
                super().__init__(*args)
                self.status_code = 400
                self.msg = msg
                self.errors = kwargs.get('errors', [])
                self.error_code = 'E_BAD_REQUEST'

        pass
