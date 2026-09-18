
from flask import render_template, request

from monitoramento import monitoramento


# Lista que armazenará temporariamente as URLs adicionadas
# Os links ficam disponíveis enquanto o Flask estiver executando
apis_adicionadas = []


def monitorar_registrar(app):

    # ROTA PRINCIPAL

    # Exibe a tela inicial do monitoramento
    @app.route("/")
    def inicio():

        # Abre o template monitorar.html
        # Enviamos a lista de APIs para exibir na página
        return render_template(
            "monitorar.html",
            apis=apis_adicionadas
        )

   
    # ROTA PARA ADICIONAR UMA API


    # Recebe a URL enviada pelo formulário
    @app.route("/adicionar", methods=["POST"])
    def adicionar_api():

        # Captura o valor digitado no campo chamado "url"
        url = request.form.get("url")

        # Verifica se a URL foi preenchida
        # Também verifica se ela ainda não está na lista
        if url and url not in apis_adicionadas:

            # Adiciona a URL à lista
            apis_adicionadas.append(url)

        # Retorna para a tela principal
        # Enviamos novamente as APIs adicionadas
        return render_template(
            "monitorar.html",
            apis=apis_adicionadas
        )
    
    # ROTA PARA MONITORAR TODAS AS APIs
    
    # Executa o monitoramento quando o botão for clicado
    @app.route("/monitorar", methods=["POST"])
    def monitorar_api():

        # Lista que armazenará os resultados
        # de todas as APIs monitoradas
        resultados = []


        # Percorre cada URL que foi adicionada
        for url in apis_adicionadas:

            # Chama a função monitoramento()
            # e envia a URL atual como argumento
            resultado = monitoramento(url)

            # Adiciona o resultado na lista
            resultados.append(resultado)


        # Retorna para a tela principal
        # Enviamos as APIs e os resultados para o HTML
        return render_template("monitorar.html", apis=apis_adicionadas, resultados=resultados)
    
    @app.route("/excluir_api/<path:url>", methods=["POST"])
    def excluir_api(url):
            
            if url in apis_adicionadas:
                
                apis_adicionadas.remove(url)

        
            return render_template("monitorar.html", apis=apis_adicionadas)