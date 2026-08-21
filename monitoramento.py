import requests
import time

from apis import apis


def monitoramento(url):

    try:
        #Aqui começa a contar o tempo de resposta da API
        inicio = time.time()

        #Ele vai pedir a API e vai esperar no máximo 10 segundos para receber uma resposta
        resposta = requests.get(url, timeout=10)

        #Aqui termina de contar o tempo de resposta da API
        fim = time.time()

        #Calcula o tempo de resposta em milissegundos
        tempo_resposta = (fim - inicio) * 1000

        if tempo_resposta < 300:
            velocidade = "RÁPIDA"

        elif tempo_resposta <= 1000:
            velocidade = "NORMAL"

        else:
            velocidade = "LENTA"


        if resposta.status_code == 200:
            status = "ONLINE"

        elif resposta.status_code >= 400 and resposta.status_code < 500:
            status = "ERRO_CLIENTE"

        elif resposta.status_code >= 500:
            status = "ERRO_SERVIDOR"

        else:
            status = "OUTRO"

        return {
            "url": url,
            "status_code":resposta.status_code,
            "tempo_resposta": tempo_resposta,
            "status": status,
            "velocidade": velocidade

        }

    except requests.exceptions.Timeout:

        return {

            "url": url,
            "status_code":None,
            "tempo_resposta": None,
            "status": "OFFLINE",
            "velocidade": None
        }

    except requests.exceptions.RequestException as erro:

        return {

            "url": url,
            "status_code":None,
            "tempo_resposta": None,
            "status": "OFFLINE",
            "erro": str(erro),
            "velocidade": None
        }


resultados = []

for api in apis:

    resultado = monitoramento(api)

    resultados.append(resultado)

for resultado in resultados:

    print("---------------------------")
    print("API: ", resultado["url"])
    print("Status HTTP: ", resultado["status_code"])
    print("Situação: ", resultado["status"])
    print("Velocidade: ", resultado["velocidade"])

    if resultado ["tempo_resposta"] is not None:
        print(f"Tempo: {resultado['tempo_resposta']:.2f} ms")
      
