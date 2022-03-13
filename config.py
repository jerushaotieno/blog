import os

class Config:

# For bblog
    SECRET_KEY=os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI=os.environ.get('SQLALCHEMY_DATABASE_URI')
    # SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://moringa:Access@localhost/pitches'
    # SQLALCHEMY_TRACK_MODIFICATIONS = False

# For Quotes
    # QUOTES_API_BASE_URL ='http://quotes.stormconsultancy.co.uk/random.json'
    # QUOTES_API_KEY = os.environ.get('QUOTES_API_KEY')
    # SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}

