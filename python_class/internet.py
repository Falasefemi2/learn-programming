import urllib.request
import json

url = "http://api.github.com"
response = urllib.request.urlopen(url)

data = json.loads(response.read().decode("utf-8"))

with open("github.json", "w") as file:
    json.dump(data, file, indent=4)

print("JSON data saved in github.json")

