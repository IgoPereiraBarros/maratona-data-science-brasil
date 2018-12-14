import re
import requests

req = requests.get('http://lacoxinha.com.br/contato')

default = re.findall(r'[\w\.-]+@[\w-]+\.[\w\.-]+', req.text)

if default:
    print(default)
else:
    print('Eeeeegua')
