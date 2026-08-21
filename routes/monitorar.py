from flask import Blueprint, render_template, request, redirect, url_for
import pyodbc
from monitoramento import monitoramento
from apis import apis

def monitorar_registrar(app):

    @app.route("/")
    def monitorar():

        resultados = []

        for api in apis:
            resultado = monitoramento(api)
            resultados.append(resultado)

        return render_template("monitorar.html", resultados=resultados)