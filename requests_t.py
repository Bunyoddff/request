import requests
import json

url='https://www.codewars.com/api/v1/users/Bunyoddff'

response=requests.get(url)
data=response.json()
print(data['clan'])