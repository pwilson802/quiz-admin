import os

class Config(object):
    # Class for adding environment variables
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'