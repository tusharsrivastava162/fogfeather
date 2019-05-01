from .base import *

DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1']

LOGIN_REDIRECT_URL = 'http://ec2-13-126-147-68.ap-south-1.compute.amazonaws.com:8800/auth/complete/google-oauth2/'