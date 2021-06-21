# API de POST

API dinâmica baseada em Flask para envio de dados a um servidor de banco de dados relacional.

## Ambiente de desenvolvimento

O Flask exige a configuração de algumas variáveis de ambiente para que o modo
de desenvolvimento seja efetivamente utilizado.

* FLASK_APP=main.py
* FLASK_ENV=development
* FLASK_DEBUG=1

Após definir as 3 variáveis de ambiente acima, usar o comando `flask run` para
iniciar o servidor no modo desenvolvimento.

## Configuração

Os dados de autenticação do servidor de banco de dados devem ser definidos
em um arquivo separado chamado `.env` na raiz da pasta do projeto. Em outros casos, os
dados também podem ser definidos nas variáveis de ambiente.

| Variável     | Descrição              |
| ------------ | ---------------------- |
| POSTAPI_DBM  | Sistema de gerenciamento de banco de dados. Opções: `postgresql`. |
| POSTAPI_DRV  | Driver ODBC utilizado. Mais informações [aqui](https://www.connectionstrings.com/).  |
| POSTAPI_SVR  | IP e porta do servidor. Separar o IP da porta com `,`. Exemplo: `192.168.1.100,1433` ou `servidor.com,4022`.
| POSTAPI_DTB  | Nome do banco de dados |
| POSTAPI_USR  | Nome do usuário        |
| POSTAPI_PSW  | Senha do usuário       |

Um exemplo de arquivo `.env` abaixo:

```text
POSTAPI_DBM=postgresql
POSTAPI_DRV={ODBC Driver 17 for SQL Server}
POSTAPI_SVR=192.168.1.100,1433
POSTAPI_DTB=Vendas
POSTAPI_USR=Gabriel
POSTAPI_PSW=123@Gab
```

## Deploy

*Em breve*

## Como usar a API

### Resumo

É necessário enviar dados no *parâmetro*, *body* e *header* da requisição para a raiz de onde o servidor está hospedado.
Por exemplo, se o servidor estiver hospedado em `localhost`, a requisição deverá ser feita para `localhost`.

**Exemplo de requisição:**

URL:

    dominio.com?tabela=vendas  

Body:

```json
[
  {
    "userId": 1,
    "id": 1,
    "title": "delectus aut autem",
    "completed": false
  },
  {
    "userId": 1,
    "id": 2,
    "title": "quis ut nam facilis et officia qui",
    "completed": false
  }
]
```

Headers:

| Chave         | Valor                               |
| ------------- | ----------------------------------- |
| Token         | eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXCJ9 |

O exemplo acima contempla apenas os dados necessários, que são:

* Parâmetro *tabela* na URL
* Conteúdo JSON no Body
* Token de acesso no Header

Os próximos tópicos contém mais detalhes sobre o uso da API.

### Parâmetros

Os parâmetros devem especificar como a aplicação vai enviar os dados.

Isso varia de acordo com o tipo de dado que será enviado, e o ideal é que cada
tipo de dado (ex: dados de relatório) seja enviado em tabelas diferentes.

O parâmetro **tabela** é obrigatório em todos os casos e deve conter o nome da tabela que vai receber
o dado enviado pelo *body*.

Abaixo está explicitado todos os parâmetros suportados:

| Parâmetro     | Descrição                           |
| ------------- | ----------------------------------- |
| tabela        | Nome da tabela que recebe os dados  |
| pk            | Nome da coluna que possui chave primária |

A combinação desses parâmetros definem como é feito o envio dos dados ao banco de dados.
Nos próximos tópicos, estão detalhadas todas combinações dos parâmetros.

#### UPSERT

Adiciona novos registros ou atualiza os registros existentes, caso já existam.

Para isso, é necessário que a tabela que deve receber os dados tenha uma coluna com **chave primária**.
O nome dessa coluna deve estar especificada no parâmetro `pk`, como no exemplo abaixo:

`dominio.com?tabela=vendas&pk=id_pedido`

### Body

O corpo da requisição deve conter uma **lista de objetos** em JSON. Mesmo que contenha apenas 
um objeto, ele deve estar dentro de uma lista.

Os nomes dos atributos das listas de objetos JSON devem conter o mesmo nome das colunas que estão no banco de dados.

```json
[
  {
    "userId": 1,
    "id": 1,
    "title": "delectus aut autem",
    "completed": false
  }
]
```

A lista acima, por exemplo, deve ser enviada na tabela abaixo:

| userId  | id   | title               | completed |
| ------- | ---- | ------------------- | --------- |
| 1       | 1    | delectus aut autem  | false     |

### Headers

O cabeçalho da requisição deve conter, obrigatoriamente, o **Token** de autenticação.



| Chave         | Descrição                           |
| ------------- | ----------------------------------- |
| Token         | Senha para autenticação obrigatória |

## Dependências

* Python 3.9.4
* Flask 1.1.2
* pyodbc 4.0.30
* Decouple 3.4
