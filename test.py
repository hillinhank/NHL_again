import requests

BASE = "https://statsapi.web.nhl.com/api/v1/"


response = requests.put(BASE + "teams")
#{"views":99, "likes":101})
print(response.json())