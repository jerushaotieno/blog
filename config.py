import os

# app = Flask(__name__)
# app.secret_key = settings.SECRET_KEY

class Config:
    '''
    General configuration parent class
    '''
    pass

    SECRET_KEY='mysecretkey'
    # SQLALCHEMY_DATABASE_URI=os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://moringa:Access@localhost/blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    UPLOADED_PHOTOS_DEST ='app/static/photos'

    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'wajowriting@gmail.com'
    MAIL_PASSWORD = 'skillsetsmatter2000'



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True


class Config:
    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True



config_options = {
'development' : DevConfig,
'production':ProdConfig
}
