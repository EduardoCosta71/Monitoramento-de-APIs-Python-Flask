import requests
import time

url = ("https://github.com/")

try:
    #Aqui começa a contar o tempo de resposta da API
    inicio = time.time()

    #Ele vai pedir a API e vai esperar no máximo 10 segundos para receber uma resposta
    resposta = requests.get(url, timeout=10)

    #Status code da resposta da API
    resposta.status_code

    # Texto da resposta da API
    resposta.text

    # JSON da resposta da API
    #resposta.json()

    #Aqui termina de contar o tempo de resposta da API
    fim = time.time()

    #Calcula o tempo de resposta em milissegundos
    tempo_resposta = (fim - inicio) * 1000

    print("API: ", url)

    print("Status: ", resposta.status_code)

    print(f"Tempo de resposta: {tempo_resposta:.2f} ms")

except requests.exceptions.Timeout:
    print("A API demorou demais para responder.")

except requests.exceptions.RequestException as erro:
    print("Não foi possivel acessar a API.")
    print(f"Erro: {erro}")
