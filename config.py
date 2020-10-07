# to run prod: export YOURAPPLICATION_SETTINGS = /path/to/config.py
class Config(object):
    DB_HOST = 'db'
    FLASK_HTPASSWD_PATH = '/secret/.htpasswd'
    # generate with something like python -c 'import os; print(os.urandom(16))'
    SECRET_KEY = 'secret'
    FLASK_SECRET = SECRET_KEY

class DevelopmentConfig(Config):
    ENV = 'development'
    DEBUG = True
    DEVELOPMENT = True

class ProductionConfig(Config):
    ENV = 'production'
    DEVELOPMENT = False
    DEBUG = False
