import requests
reponse=requests.get('http://127.0.0.1:8000/')
print(reponse.json())