import requests

BASE = "http://127.0.0.1:5000/"
# send a request to the url that is base url plus helloworld
respone = requests.post(BASE + "helloworld")
print(respone.json())