import requests
import json
response=requests.get('https://api.stackexchange.com/2.3/articles/1?page=1&pagesize=4&fromdate=1690848000&todate=1690848000&order=desc&min=1690848000&max=1690848000&sort=activity&site=stackoverflow')
print(response.json())