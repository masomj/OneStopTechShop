from django.conf import settings
from storages.backends.s3boto3 import S3BotoS3storage

class StaticStorage(S3BotoS3storage):
    location = settings.STATICFILES_LOCATION    

class MediaStorage(S3BotoS3storage):
    location = settings.MEDIAFILES_LOCATION    
    