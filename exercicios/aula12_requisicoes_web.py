import requests
import time

text = []

try:
    req = requests.put('https://g1.com.br')
    text.append(req.text)
except Exception as e:
    text.append(e)

for i in text:
    print(text)
