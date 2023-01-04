import requests

BASE = "http://127.0.0.1:5000/"

data = [{"likes":10, "name":"words", "views": 143245},
{"likes":378899, "name":"how to develop python", "views": 111},
{"likes":4389, "name":"Tim sings", "views": 133333},
{"likes":1050, "name":"Tim doesnt", "views": 1222222}]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())



response = requests.delete(BASE + "video/0")
print(response)
input()
response = requests.get(BASE + "video/2")
print(response.json())