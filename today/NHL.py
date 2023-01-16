import requests
from config import NHL_ACCESS_KEY

class N2_API:
    def __init__(self):
        params={NHL_ACCESS_KEY}

        url= 'https://statsapi.web.nhl.com/api/v1/conferences'
        results = requests.get(url)
        #results = requests.get('https://statsapi.web.nhl.com/api/v1/conferences')
        return results.json()

