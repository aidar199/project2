import requests
import requests.auth


session = requests.Session()

basic = requests.auth.HTTPBasicAuth('Айдар'.encode('UTF-8'), '')

#session.auth = ('Айдар', '')
#auth = session.post('http://localhost/client')
res = session.get('http://localhost/client/hs/client/clients?name=Кармаскалы', auth=basic)
print(res.status_code)
print(res.text)