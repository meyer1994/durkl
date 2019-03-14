import os

# Use to create the local, usually for testing, database
basedir = os.path.abspath(os.path.dirname(__file__))
SQLITE_MEM = 'sqlite://'


class Config(object):
    '''
    Basic configuration objecct for flask instance app.
    '''

    # The environment variable DATABASE_URL is used in Heroku when setting
    # their database system
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or SQLITE_MEM
    SQLALCHEMY_TRACK_MODIFICATIONS = False
