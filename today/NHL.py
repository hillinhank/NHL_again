import requests
from config import NHL_ACCESS_KEY

class N2_API:
    def get(self, name):
        params={}

        #url= "https://statsapi.web.nhl.com/"
        results = requests.get('https://statsapi.web.nhl.com/api/v1/conferences')
        #results = requests.get('https://statsapi.web.nhl.com/api/v1/conferences')
        return results.json()

