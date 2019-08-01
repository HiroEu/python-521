import requests
DOMAIN_URL = 'https://gen-net.herokuapp.com/api/users/'

payload = {


'name': input('Digite seu Nome: '),

'email': input('Digite seu email: '),  

'password': input('Digite sua senha: ') 

}                                                                                             

response = requests.post(DOMAIN_URL, payload)

if response.status_code == 200:
   user_id = response.json().get('id')
   print('Usuario {} cadastrado com sucesso'.format(user_id))
else:
   print(response.text) 







