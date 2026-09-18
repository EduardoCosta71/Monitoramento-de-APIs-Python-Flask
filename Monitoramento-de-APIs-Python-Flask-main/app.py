
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for, session
import re
import os


app = Flask (__name__)

from routes.monitorar import monitorar_registrar


monitorar_registrar(app)

if __name__ == "__main__":
    app.run(debug=True)