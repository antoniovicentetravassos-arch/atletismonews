from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def obter_titulos():
    url = "https://fpatletismo.pt/categoria/noticias/"
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    titulos = []

    for h2 in soup.find_all("h2"):
        a = h2.find("a")
        if a and a.text.strip():
            titulos.append(a.text.strip())

    return titulos 

def obter_imagens():
    url = "https://fpatletismo.pt/categoria/noticias/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    imagens = []

    for img in soup.find_all("img"):
        src = img.get("src")
        if src:
            imagens.append(src)

    return imagens[:5] #apenas 5 imagens

@app.route("/api/noticias", methods=["GET"])
def noticias():
    return jsonify(obter_titulos())

@app.route("/api/imagens", methods=["GET"])
def imagens():
    return jsonify(obter_imagens())

if __name__ == "__main__":
    app.run(debug=True)
