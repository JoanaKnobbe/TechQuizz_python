import requests
import random

url = 'https://raw.githubusercontent.com/guilhermeonrails/api-imersao-ia/main/words.json'
response = requests.get(url)
data = response.json()
len(data)
valor_secreto = random.choice(data)

palavra_secreta = valor_secreto['palavra']
dica = valor_secreto['dica']
print(f'A palavra secreta tem {len(palavra_secreta)} letras -> E a dica é: {dica}')

resposta = input('Qual é a tecnologia?')
resposta = resposta.lower()
if resposta == palavra_secreta:
    print('Parabéns! Você acertou :)')
else: 
    print(f'Game Over -- A palavra certa era "{palavra_secreta}"')
