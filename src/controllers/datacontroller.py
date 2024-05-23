from .basecontroller import BaseController

class DataController(BaseController):

    def __init__(self):
        super().__init__()
    
    
    def validate_uploaded_file(self, file):

        if file.split('.')[-1] not in self.app_settings.FILE_ALLOWED_TYPES:
            return False, ""#ResponseSignal.FILE_TYPE_NOT_SUPPORTED.value

        return ''#True, ResponseSignal.FILE_VALIDATED_SUCCESS.value

