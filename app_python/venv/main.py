import requests

resultado = requests.get('https://meiobit.com/')
print(resultado.text)