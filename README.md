# API de POST para SQL Server

API dinâmica baseada em Flask para envio de dados ao servidor SQL Server.

## Ambiente de desenvolvimento

*Em breve*

## Configuração

*Em breve*

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

*Em breve*

### Body

*Em breve*

### Headers

*Em breve*

| Chave         | Descrição                           |
| ------------- | ----------------------------------- |
| Token         | Senha para autenticação obrigatória |

## Dependências

* Python 3.9.4
* Flask 1.1.2