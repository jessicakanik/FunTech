import requests

responce = requests.get("https://github.com/jessicakanik/FunTech/tree/master")
print(responce.status_code)
if responce.status_code != 200:
    quit(0)
else:
    print(responce)