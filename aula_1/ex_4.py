import requests
URL = 'https://gen-net.herokuapp.com/api/users/{}'

name = input('Digite Nome: ')

response = requests.get(URL.format(name)) 

print(response.json())





