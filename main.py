from flask import Flask, render_template, redirect, request, flash
import database.views as views

app = Flask(__name__)
app.secret_key = 'a3f9c1b8e7d4f6a9b2'

@app.route('/')
def home():
    pesquisa = request.args.get('pesquisa', '')

    if pesquisa:
        produtos = views.get_produtos_busca(pesquisa)
    else:
        produtos = views.get_all()

    return render_template('index.html', produtos=produtos, texto_pesquisa=pesquisa)


@app.route('/criar', methods=['GET'])
def get_criar():
    dict_tipos = views.get_tipos()
    return render_template('novo.html', dict_tipos=dict_tipos)


@app.route('/criar', methods=['POST'])
def post_criar():
    dados = request.form
    try:
        views.post_produto(dados)
        flash('Produto criado com sucesso!', 'success')
    except Exception as e:
        print(f'Erro ao criar produto: {e}')
        flash('Erro ao criar produto.', 'error')
    return redirect('/')


@app.route('/editar/<int:produto_id>', methods=['GET'])
def get_editar(produto_id):
    produto = views.get_produto(produto_id)
    dict_tipos = views.get_tipos()

    if not produto:
        flash('Produto não encontrado.', 'error')
        return redirect('/')

    return render_template('update.html', produto=produto, dict_tipos=dict_tipos)


@app.route('/editar/<int:produto_id>', methods=['POST'])
def put_editar(produto_id):
    dados = request.form
    try:
        views.put_produto(produto_id, dados)
        flash('Produto atualizado com sucesso!', 'success')
    except Exception as e:
        print(f'Erro ao atualizar produto: {e}')
        flash('Erro ao atualizar produto.', 'error')
    return redirect('/')


@app.route('/deletar/<int:produto_id>', methods=['POST'])
def delete(produto_id):
    try:
        views.delete_produto(produto_id)
        flash('Produto deletado com sucesso!', 'success')
    except Exception as e:
        print(f'Erro ao deletar produto: {e}')
        flash('Erro ao deletar produto.', 'error')
    return redirect('/')


if __name__ == '__main__':
    app.run()
