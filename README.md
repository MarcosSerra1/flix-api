# Projeto de API com Django

Este projeto é uma API desenvolvida apenas com Django, como parte do curso "Django Master" ministrado pelo professor Felipe Azambuja da PycodeBR. A API não utiliza Django REST Framework (DRF) e demonstra como criar endpoints de API básicos utilizando as funcionalidades nativas do Django.

## Estrutura do Projeto

- `app/`: Diretório do projeto principal Django.
- `genres/`: Aplicativo Django responsável por gerenciar gêneros.
- `requirements.txt`: Arquivo contendo as dependências do projeto.

## Configuração Inicial

1. Clone o repositório:

   ```bash
   git clone https://github.com/MarcosSerra1/flix-api.git
   ```
2. Crie e ative um ambiente virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
   ```
3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```
4. Aplique as migrações do banco de dados:

   ```bash
   python manage.py migrate
   ```
5. Inicie o servidor de desenvolvimento:

   ```bash
   python manage.py runserver
   ```

## Endpoints da API

### Listar e Criar Gêneros

- **URL:** `/genres/`
- **Métodos Suportados:** `GET`, `POST`

#### GET

Retorna uma lista de todos os gêneros.

#### POST

Cria um novo gênero.

**Exemplo de Corpo de Requisição (POST):**

```json
{
    "name": "Nome do Gênero"
}
```

### Detalhar, Atualizar e Excluir Gêneros

- **URL:** `/genres/<int:pk>/`
- **Métodos Suportados:** `GET`, `PUT`, `DELETE`

#### GET

Retorna os detalhes de um gênero específico.

#### PUT

Atualiza os detalhes de um gênero específico.

**Exemplo de Corpo de Requisição (PUT):**

```json
{
    "name": "Nome Atualizado do Gênero"
}
```

#### DELETE

Exclui um gênero específico.

## Arquivos Importantes

### `genres/views.py`

Contém as views para os endpoints da API:

- `genre_create_list_view`: Gerencia requisições GET para listar gêneros e POST para criar novos gêneros.
- `genre_detail_view`: Gerencia requisições GET para detalhar, PUT para atualizar e DELETE para excluir gêneros específicos.

### `genres/urls.py`

Define as rotas para os endpoints da API:

```python
from django.urls import path
from genres.views import genre_create_list_view, genre_detail_view

urlpatterns = [
    path('genres/', genre_create_list_view, name='genre'),
    path('genres/<int:pk>/', genre_detail_view, name='genre-detail-view'),
]
```

## Observações

- Esta API foi desenvolvida utilizando apenas as funcionalidades básicas do Django, sem o uso de Django REST Framework (DRF).
- Para proteger endpoints que modificam dados (POST, PUT, DELETE), o decorador `@csrf_exempt` foi utilizado para desabilitar a verificação CSRF temporariamente. Em um ambiente de produção, considere implementar uma abordagem mais segura.

## Licença

Este projeto está licenciado sob os termos da licença MIT.
