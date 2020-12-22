import datetime


class Marketplace:
    def __init__(self, name: str):
        self.__name = name

    def get_name(self) -> str:
        return self.__name

    def __str__(self) -> str:
        return f"""
                {self.__name}
                """


class Category:
    def __init__(self, category: str, parent: Marketplace):
        self.__parent = parent
        self.__category_name = category

    def get_parent_name(self) -> str:
        return self.__parent.get_name()

    def get_name(self) -> str:
        return self.__category_name

    def __str__(self):
        return f"""
                MarketPlace: {self.__parent.get_name()}
                Category name: {self.__category_name}
                """


class Subcategory(Category):
    def __init__(self, subcategory: str, category: Category):
        self.__category = category
        self.__sub_name = subcategory

    def get_name(self):
        return self.__sub_name

    def get_cat_name(self):
        return self.__category.get_name()

    def __str__(self):
        return f"""
                Marketplace name: {self.__category.get_parent_name()}
                Category: {self.__category.get_name()}
                SubCategory: {self.__sub_name}
                """


class Dados:
    def set_marketplaces(market):
        if market is not None and market == "":
            return None
        arquivo = open('dados/marketplaces.txt', 'r')
        for linha in arquivo:
            linha = linha.strip()
            print(linha.lower(), market.lower())
            if linha.lower() == market.lower():
                return None
        arquivo = open('dados/marketplaces.txt', 'a')
        arquivo.write(f'\n{market}')

    def get_marketplaces() -> list:
        lista_marketplaces = []
        arquivo = open('dados/marketplaces.txt', 'r')
        for linha in arquivo:
            linha = linha.strip()
            linha = {'name': linha}
            lista_marketplaces.append(linha)
        arquivo.close()
        return lista_marketplaces

    def set_categorias(market, categoria):
        if categoria is not None and categoria == "":
            return None
        arquivo = open('dados/categorias.txt', 'r')
        for linha in arquivo:
            linha = linha.strip()
            linha = linha.split(';')
            if linha[1].lower() == categoria.lower() and linha[0] == market:
                return None
        arquivo = open('dados/categorias.txt', 'a')
        arquivo.write(f'\n{market};{categoria}')

    def get_categorias() -> list:
        lista_categorias = []
        arquivo = open('dados/categorias.txt', 'r')
        for linha in arquivo:
            linha = linha.strip()
            linha_dados = linha.split(';')
            linhas_formatadas = {
                'referencia': linha_dados[0],
                'nome': linha_dados[1]
            }
            lista_categorias.append(linhas_formatadas)
        arquivo.close()
        return lista_categorias

    def set_subcategorias(categoria, sub):
        if sub is None or sub == "":
            return None
        arquivo = open('dados/subCategorias.txt', 'r')
        for linha in arquivo:
            linha = linha.strip()
            linha = linha.split(';')
            if linha[1].lower() == sub.lower() and linha[0] == categoria:
                return None
        arquivo = open('dados/subCategorias.txt', 'a')
        arquivo.write(f'\n{categoria};{sub}')

    def get_subcategorias() -> list:
        lista_sub = []
        arquivo = open('dados/subCategorias.txt', 'r')
        for linha in arquivo:
            linha = linha.strip()
            linha_dados = linha.split(';')
            linhas_formatadas = {
                'referencia': linha_dados[0],
                'nome': linha_dados[1]
            }
            lista_sub.append(linhas_formatadas)
        arquivo.close()
        return lista_sub

    def log_historico(acao) -> None:
        arquivo = open('dados/logsistema.txt', 'a')
        data = datetime.datetime.utcnow()
        data = data.strftime("%d/%m/%Y Hora %H:%M")
        arquivo.write(f'{data} acao: {acao} \n')
        arquivo.close()
