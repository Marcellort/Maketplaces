import Classes
from flask import Flask, render_template, request

marketplaces = []
cat = []
sub = []


def carregar_listas():
    marketplaces.clear()
    cat.clear()
    sub.clear()
    dados_categorias = Classes.Dados.get_categorias()
    dados_marketplaces = Classes.Dados.get_marketplaces()
    dados_subCategorias = Classes.Dados.get_subcategorias()

    for i in dados_marketplaces:
        marketplaces.append(Classes.Marketplace(i['name']))

    for i in dados_categorias:
        for a in marketplaces:
            if i['referencia'] == a.get_name():
                cat.append(Classes.Category(i['nome'], a))

    for i in dados_subCategorias:
        for a in cat:
            if i['referencia'] == a.get_name():
                sub.append(Classes.Subcategory(i['nome'], a))
                break


app = Flask(__name__)


@app.route('/')
def index():
    carregar_listas()
    Classes.Dados.log_historico('Listando MarketPlaces')
    return render_template('index.html', marketplaces=marketplaces)


@app.route('/categorias/<market>')
def categorias(market):
    carregar_listas()
    Classes.Dados.log_historico(f'Listando categorias no Marketplace {market}')
    return render_template('categoria.html', cat=cat, market=market)


@app.route('/subcategorias/<cat>/<market>')
def subcategorias(cat, market):
    carregar_listas()
    Classes.Dados.log_historico(f'Listando subcategorias da categoria: {cat} no Marketplace: {market}')
    return render_template('subcategoria.html', sub=sub, category=cat, mkt=market)


@app.route('/cadastrar_marketplace')
def cadastro_Marketplace():
    carregar_listas()
    menssagem = ''
    marketplace_add = request.args.get('market')
    if marketplace_add is not None:
        print(marketplace_add)
        Classes.Dados.set_marketplaces(marketplace_add)
        menssagem = f'{marketplace_add} cadastrado com sucesso'
    Classes.Dados.log_historico(f'Carregando tela de resgistro de marketplaces')
    return render_template('cadastro_marketplace.html',menssagem=menssagem)

@app.route('/cadastrar_categoria')
def cadastro_Categoria():
    carregar_listas()
    menssagem = ''
    marketplace_add = request.args.get('mkt')
    categoria_add = request.args.get('cat')
    if categoria_add is not None:
        Classes.Dados.set_categorias(marketplace_add, categoria_add)
        menssagem = f'{categoria_add} cadastrado com sucesso'
    Classes.Dados.log_historico(f'Carregando tela de resgistro de categorias')
    return render_template('cadastro_categoria.html', market=marketplaces, menssagem= menssagem)

@app.route('/cadastrar_subcategoria')
def cadastro_subCategoria():
    carregar_listas()
    menssagem = ''
    categoria_add = request.args.get('cat')
    sub_add = request.args.get('sub')
    if sub_add is not None:
        Classes.Dados.set_subcategorias(categoria_add, sub_add)
        menssagem = f'{sub_add} cadastrado com sucesso'
    Classes.Dados.log_historico(f'Carregando tela de resgistro de sub categorias')
    return render_template('cadastro_subcategoria.html', cat=cat, menssagem = menssagem)


app.run(debug=True)
