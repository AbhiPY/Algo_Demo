import os

class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or b'\xed)\xf8\xa1\xf4\x0fk\xa8\xdd\x92\xb6O\x066\xb8\x8f'
    MONGODB_SETTINGS = {'db': 'POC_Dashboard'}
