import requests
import requests.auth


session = requests.Session()

basic = requests.auth.HTTPBasicAuth('Айдар'.encode('UTF-8'), '')

#session.auth = ('Айдар', '')
#auth = session.post('http://localhost/client')
<<<<<<< HEAD
res = session.get('http://localhost/client/hs/client/clients?name=Кармаскал', auth=basic)
=======
res = session.get('http://localhost/client/hs/client/clients?name=Кармаскалы', auth=basic)
>>>>>>> f4f810f91d3d4ece6709eaa51129705e3c3ead08
print(res.status_code)
print(res.text)