import requests

def fuck():
    print("Fuck Conda!")

def request():
    r = requests.get("https://google.com")
    print(r.text)
