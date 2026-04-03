from itertools import product

from flask import Flask, render_template, redirect, request
import database.views as views
from database.create_tables import create_tables

app = Flask(__name__)


@app.route('/')
def home():
    pesquisa = request.args.get('pesquisa')

    if pesquisa:
        produtos = views.get_produtos_busca(pesquisa)
    else:
        produtos = views.get_all()

    return render_template('index.html', produtos=produtos)


@app.route('/criar', methods=['GET'])
def get_criar():
    dict_tipos = views.get_tipos()
    return render_template('novo.html', dict_tipos=dict_tipos)


@app.route('/criar', methods=['POST'])
def post_criar():
    dados = request.form
    views.post_produto(dados)
    return redirect('/')


@app.route('/editar/<int:produto_id>', methods=['GET'])
def get_editar(produto_id):
    produto = views.get_produto(produto_id)
    dict_tipos = views.get_tipos()
    return render_template('update.html', produto=produto, dict_tipos=dict_tipos)


@app.route('/editar/<int:produto_id>', methods=['POST'])
def put_editar(produto_id):
    dados = request.form
    views.put_produto(produto_id, dados)
    return redirect('/')


@app.route('/deletar/<int:produto_id>', methods=['POST'])
def delete(produto_id):
    views.delete_produto(produto_id)
    return redirect('/')


if __name__ == '__main__':
    create_tables()
    app.run()
