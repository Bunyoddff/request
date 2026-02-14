import requests


url='https://www.codewars.com/api/v1/users/Bunyoddff'

response=requests.get(url)

print(response.status_code)