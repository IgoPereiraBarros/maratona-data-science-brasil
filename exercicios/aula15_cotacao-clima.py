import requests
import json
import time
import datetime

def cotacao(city, key='a0551115d16740758a3a004849e9149a'):
    req = requests.get('http://api.openweathermap.org/data/2.5/weather?q={}&APPID={}'.format(city, key))
    cot = json.loads(req.text)
    return cot

teresina = cotacao('teresina')

print(teresina['weather'][0]['main'])
