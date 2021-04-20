import pyodbc
from decouple import config


class PostgreSQL:
    def __init__(self, conexao):
        self.cursor = conexao.cursor()

    def upsert(self, tabela, dados: list, pk):
        """ :param tabela: Nome da tabela para recebimento dos dados
            :param dados: Lista dos dados que devem ser enviados ao banco de dados
            :param pk: Chave primária necessária para fazer o update
        """
        colunas_virg_verif = ','.join(dados[0].keys())  # colunas para verificação separadas por vírgula
        for dado in dados:

            # parte das colunas
            colunas = dado.keys()
            colunas_virg = ','.join(map(str, colunas))  # colunas separadas por vírgula
            if colunas_virg != colunas_virg_verif:
                raise AttributeError(
                    f'Houve divergência entre as colunas! A coluna "{colunas_virg}" é diferente da '
                    f'coluna de verificação "{colunas_virg_verif}". Verifique se todos os objetos '
                    f'contidos no JSON enviado possuem os mesmo atributos.')

            # parte dos valores
            valores = dado.values()  # extrai os valores do objeto
            # adiciona aspas simples nas strings
            valores = list(map(lambda x: f"'{x}'" if isinstance(x, str) else x, valores))
            # converte None para null
            valores = list(map(lambda x: 'null' if x is None else x, valores))
            # separa os valores por vírgula
            valores_virg = ','.join(map(str, valores))

            # parte do update
            update = ''
            for n in range(len(colunas)):
                # transforma variáveis em lista para se tornarem indexáveis e incrementa no update
                update += f' {list(colunas)[n]} = {list(valores)[n]},'
            update = update.strip(',')  # remove a última vírgula do update

            # cria a consulta e executa
            self.cursor.execute(
                f'INSERT INTO {tabela}({colunas_virg}) VALUES ({valores_virg}) ON CONFLICT ({pk}) '
                f'DO UPDATE SET{update};')
        self.cursor.commit()


def conectar():
    sgbd = config("POSTAPI_DBM")
    driver = config("POSTAPI_DRV")
    servidor = config("POSTAPI_SVR")
    banco = config("POSTAPI_DTB")
    usuario = config("POSTAPI_USR")
    senha = config("POSTAPI_PSW")

    conexao = pyodbc.connect(f'DRIVER={driver};SERVER={servidor};DATABASE={banco};UID={usuario};PWD={senha}')

    if sgbd == 'postgresql':
        return PostgreSQL(conexao)
    else:
        raise ValueError('Parâmetro "POSTAPI_DBM" inválido! Consulte a documentação para obter a lista dos sistemas '
                         'gerenciadores de banco de dados suportados.')
