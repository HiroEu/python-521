import requests
DOMAIN_URL = 'https://gen-net.herokuapp.com/api/users/{}'

user_id = input('Digite seu id: ')


response = requests.put(DOMAIN_URL.format(user_id))

if response.status_code == 200:
   print(response.json().get('name')) 
else:
   print(response.text) 

   


