from decouple import config
import mysql.connector


class Mysql:
    def __init__(self, conexao):
        self.cursor = conexao.cursor()

    def upsert(self, tabela, dados: list):
        """ :param tabela: Nome da tabela para recebimento dos dados
            :param dados: Lista dos dados que devem ser enviados ao banco de dados
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

            # cria a consulta e executa
            self.cursor.execute(
                f'REPLACE INTO {tabela}({colunas_virg}) VALUES ({valores_virg})')
        self.cursor.commit()


def enviar_dados(tabela, dados):
    host = config("POSTAPI_HST")
    porta = config("POSTAPI_PRT", 3306)
    banco = config("POSTAPI_DTB")
    usuario = config("POSTAPI_USR")
    senha = config("POSTAPI_PSW")

    # With usado para fechar a conexão e evitar erros de transações
    with mysql.connector.connect(host=host, port=porta, user=usuario, password=senha, db=banco) as conexao:
        return Mysql(conexao).upsert(tabela, dados)
