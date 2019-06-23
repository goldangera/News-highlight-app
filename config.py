import os

class Config:
    '''
    General confirguration parent class
    '''

    NEWS_API_BASE_URL = "https://newsapi.org/v2/{}?country=us&apiKey={}"
    
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')    