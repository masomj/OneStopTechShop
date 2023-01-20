from django.conf import settings
from storages.backends.s3boto3 import s3botoS3storage

class StaticStorage(s3botoS3storage):
    location = settings.STATICFILES_LOCATION    

class MediaStorage(s3botoS3storage):
    location = settings.MEDIAFILES_LOCATION    
    