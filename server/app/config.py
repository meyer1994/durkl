import os

SQLITE_MEM = 'sqlite://'


class ProductionConfig(object):
    ''' Basic configuration object for production '''
    ENV = 'production'
    DEBUG = False
    TESTING = False

    SECRET_KEY = os.urandom(16)

    # The environment variable DATABASE_URL is used in Heroku when setting
    # their database system
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(object):
    ''' Basic configuration objecct for development '''
    ENV = 'development'
    DEBUG = True
    TESTING = False

    SECRET_KEY = 'some_key'

    # The environment variable DATABASE_URL is used in Heroku when setting
    # their database system
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class TestConfig(object):
    ''' Basic configuration objecct for testing '''
    ENV = 'development'
    DEBUG = True
    TESTING = True

    SECRET_KEY = 'some_key'

    # The environment variable DATABASE_URL is used in Heroku when setting
    # their database system
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
