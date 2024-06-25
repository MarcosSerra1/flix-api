# Projeto de API com Django
Este projeto é uma API desenvolvida com Django e Django REST Framework (DRF), como parte do curso "Django Master" ministrado pelo professor Felipe Azambuja da PycodeBR. A API utiliza Django e DRF e demonstra como criar endpoints de API utilizando as funcionalidades do DRF.

## Estrutura do Projeto
- app/: Diretório do projeto principal Django.
- genres/: Aplicativo Django responsável por gerenciar gêneros.
- actors/: Aplicativo Django responsável por gerenciar atores.
- requirements.txt: Arquivo contendo as dependências do projeto.

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

Retorna uma mensagem de sucesso ou erro

```json
{
    "message": "Gênero deletado com sucesso."
}
```

ou

```json
{
    "error": "Error"
}
```

## Arquivos Importantes

### `genres/views.py`

Contém as views para os endpoints da API:

- `GenreCreateListView`: Gerencia requisições GET para listar gêneros e POST para criar novos gêneros.
- `GenreRetrieveUpdateDestroyView`: Gerencia requisições GET para detalhar, PUT para atualizar e DELETE para excluir gêneros específicos.

### `genres/urls.py`

Define as rotas para os endpoints da API:

```python
from django.urls import path
from genres.views import GenreCreateListView, GenreRetrieveUpdateDestroyView

urlpatterns = [
    path('genres/', GenreCreateListView, name='genre'),
    path('genres/<int:pk>/', GenreRetrieveUpdateDestroyView, name='genre-detail-view'),
]
```
---

### Listar e Criar Atores

- **URL:** `/actors/`
- **Métodos Suportados:** `GET`, `POST`

#### GET

Retorna uma lista de todos os atores.

#### POST

Cria um novo ator.

**Exemplo de Corpo de Requisição (POST):**

```json
{
    "name": "Nome do Ator",
    "birthday": "Data de Nascimento do Ator",
    "nationality": "País de Nascimento do Ator"
}
```

### Detalhar, Atualizar e Excluir Ator

- **URL:** `/genres/<int:pk>/`
- **Métodos Suportados:** `GET`, `PUT`, `DELETE`

#### GET

Retorna os detalhes de um ator específico.

#### PUT

Atualiza os detalhes de um ator específico.

**Exemplo de Corpo de Requisição (PUT):**

```json
{
    "name": "Nome Atualizado do Ator",
    "birthday": "Data de Nascimento Atualizado do Ator",
    "nationality": "País de Nascimento Atualizado do Ator"
}
```

#### DELETE

Exclui um ator específico.

Retorna uma mensagem de sucesso ou erro

```json
{
    "message": "Ator deletado com sucesso."
}
```

ou

```json
{
    "error": "Error"
}
```

## Arquivos Importantes

### `actors/views.py`

Contém as views para os endpoints da API:

- `ActorCreateListView`: Gerencia requisições GET para listar atores e POST para criar novos atores.
- `ActorRetrieveUpdateDestroyView`: Gerencia requisições GET para detalhar, PUT para atualizar e DELETE para excluir atores específicos.

### `actors/urls.py`

Define as rotas para os endpoints da API:

```python
from django.urls import path
from actors.views import ActorCreateListView, ActorRetrieveUpdateDestroyView

urlpatterns = [
    path('actors/', ActorCreateListView.as_view(), name='actor-create-list'),
    path('actors/<int:pk>/', ActorRetrieveUpdateDestroyView.as_view(), name='actor-detail-view'),
]
```

## Licença

Este projeto está licenciado sob os termos da licença MIT.
