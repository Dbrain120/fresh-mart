import os
basedir = os.path.abspath(os.path.dirname(__file__)) #Tells pyhton to look at all files OS

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or'you will never guess'  # it's better to use config.py than this one
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False