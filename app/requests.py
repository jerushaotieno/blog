import urllib.request,json
from .models import Blog
from .models import Quotes
from urllib import response


# Getting api key
api_key = None
# Getting the blog base url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['BLOG_API_KEY']
    base_url = app.config['BLOG_API_BASE_URL']



base_url = 'http://quotes.stormconsultancy.co.uk/random.json'

def get_random_quote():
    url = base_url 

    response = urllib.request.urlopen(url)
    data= json.loads(response.read())
    quote_details=[]

    author = data.get('author')
    quote = data.get('quote')

    new_quote= Quotes(author, quote)
    quote_details.append(new_quote)

    return quote_details 