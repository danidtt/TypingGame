# No terminal, instale requests com o comando: pip install requests

import requests
import random
import time

url = 'http://www.mit.edu/~ecprice/wordlist.10000'

resposta = requests.get(url)
palavras = resposta.content.splitlines()

palavras = [palavra.decode('utf-8') for palavra in palavras]

randomWords = random.sample(palavras, 10)

pontos = 0
tic = time.perf_counter()

for palavra in randomWords:
    print(palavra)
    entrada = input()
    if entrada == palavra:
        pontos = pontos + 1

tac = time.perf_counter()

print(pontos)
print(tac-tic)
