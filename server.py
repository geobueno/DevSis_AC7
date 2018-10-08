from flask import Flask
from flask import render_template

import pandas as pd
from matplotlib import pyplot as Mplt
import seaborn as sb
import xlrd

Dados = pd.read_excel('static\PesquisaAuto.xlsx', 'Pesquisa')

Mplt.hist(Dados["Imagem"], bins=5)

Mplt.savefig('static\histograma.jpg')

sb.jointplot(x="Preco", y="Imagem", data=Dados)

Mplt.savefig('static\dispersao.jpg')

app = Flask(__name__)

@app.route ("/histograma", methods=["GET"])
def histograma():
    return render_template("histograma.html")

@app.route ("/dispersao", methods=["GET"])
def dispersao():
    return render_template("dispersao.html")

if __name__ == "__main__":
    app.run(port=80)
