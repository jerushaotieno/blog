import os

class Config:

    QUOTES_API_BASE_URL ='http://quotes.stormconsultancy.co.uk/random.json'
    QUOTES_API_KEY = os.environ.get('QUOTES_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

