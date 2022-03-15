import os

app = Flask(__name__)
app.secret_key = settings.SECRET_KEY

class Config:
    '''
    General configuration parent class
    '''
    pass

    SECRET_KEY=os.environ.get('SECRET_KEY')
    # SQLALCHEMY_DATABASE_URI=os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://moringa:Access@localhost/blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    UPLOADED_PHOTOS_DEST ='app/static/photos'



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

config_options = {
'development' : DevConfig,
'production':ProdConfig
}
