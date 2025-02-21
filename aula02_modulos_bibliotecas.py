import math
import random
import datetime

print(math.sqrt(16))

# random
print(random.randint(1, 10))


# datetime
agora = datetime.datetime.now()

print("Data e hora atual:", agora)

#pip install requests

import requests
import json
resposta = requests.get("https://parallelum.com.br/fipe/api/v1/carros/marcas")

print("Status da Requisição:", resposta.status_code)

#print("Resposta da API:", resposta.json())
print(json.dumps(resposta.json(), indent=4))