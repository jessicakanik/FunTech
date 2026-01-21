import requests

response = requests.get("https://github.com/jessicakanik/FunTech/tree/master")
print(response.status_code)
if response.status_code != 200:
    quit(0)
else:
    print(response)