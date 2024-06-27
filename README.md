# Projeto de API com Django

Este projeto é uma API desenvolvida com Django e Django REST Framework (DRF), como parte do curso "Django Master" ministrado pelo professor Felipe Azambuja da PycodeBR. A API utiliza Django e DRF e demonstra como criar endpoints de API utilizando as funcionalidades do DRF.

## Estrutura do Projeto

- `app/`: Diretório do projeto principal Django.
- `genres/`: Aplicativo Django responsável por gerenciar gêneros.
- `actors/`: Aplicativo Django responsável por gerenciar atores.
- `movies/`: Aplicativo Django responsável por gerenciar filmes.
- `reviews/`: Aplicativo Django responsável por gerenciar reviews.
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

**Resposta de Sucesso:**

```json
{
    "message": "Gênero deletado com sucesso."
}
```

**Resposta de Erro:**

```json
{
    "error": "Erro"
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
    path('genres/', GenreCreateListView.as_view(), name='genre-create-list'),
    path('genres/<int:pk>/', GenreRetrieveUpdateDestroyView.as_view(), name='genre-detail-view'),
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

- **URL:** `/actors/<int:pk>/`
- **Métodos Suportados:** `GET`, `PUT`, `DELETE`

#### GET

Retorna os detalhes de um ator específico.

#### PUT

Atualiza os detalhes de um ator específico.

**Exemplo de Corpo de Requisição (PUT):**

```json
{
    "name": "Nome Atualizado do Ator",
    "birthday": "Data de Nascimento Atualizada do Ator",
    "nationality": "País de Nascimento Atualizado do Ator"
}
```

#### DELETE

Exclui um ator específico.

**Resposta de Sucesso:**

```json
{
    "message": "Ator deletado com sucesso."
}
```

**Resposta de Erro:**

```json
{
    "error": "Erro"
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

---

### Listar e Criar Filmes

- **URL:** `/movies/`
- **Métodos Suportados:** `GET`, `POST`

#### GET

Retorna uma lista de todos os filmes.

#### POST

Cria um novo filme.

**Exemplo de Corpo de Requisição (POST):**

```json
{
    "title": "Nome do Filme",
    "release_date": "Data de lançamento do Filme",
    "resume": "Sinopse do Filme",
    "genre": "Gênero do Filme",
    "actors": ["Lista com nomes dos Atores do Filme"]
}
```

### Detalhar, Atualizar e Excluir Filme

- **URL:** `/movies/<int:pk>/`
- **Métodos Suportados:** `GET`, `PUT`, `DELETE`

#### GET

Retorna os detalhes de um filme específico.

#### PUT

Atualiza os detalhes de um filme específico.

**Exemplo de Corpo de Requisição (PUT):**

```json
{
    "title": "Nome do Filme Atualizado",
    "release_date": "Data de lançamento do Filme Atualizado",
    "resume": "Sinopse do Filme Atualizado",
    "genre": "Gênero do Filme Atualizado",
    "actors": ["Lista com nomes dos Atores do Filme Atualizado"]
}
```

#### DELETE

Exclui um filme específico.

**Resposta de Sucesso:**

```json
{
    "message": "Filme deletado com sucesso."
}
```

**Resposta de Erro:**

```json
{
    "error": "Erro"
}
```

## Arquivos Importantes

### `movies/views.py`

Contém as views para os endpoints da API:

- `MovieCreateListView`: Gerencia requisições GET para listar filmes e POST para criar novos filmes.
- `MovieRetrieveUpdateDestroyView`: Gerencia requisições GET para detalhar, PUT para atualizar e DELETE para excluir filmes específicos.

### `movies/urls.py`

Define as rotas para os endpoints da API:

```python
from django.urls import path
from movies.views import MovieCreateListView, MovieRetrieveUpdateDestroyView

urlpatterns = [
    path('movies/', MovieCreateListView.as_view(), name='movies-create-list'),
    path('movies/<int:pk>/', MovieRetrieveUpdateDestroyView.as_view(), name='movies-detail-view'),
]
```

---

### Listar e Criar Reviews

- **URL:** `/reviews/`
- **Métodos Suportados:** `GET`, `POST`

#### GET

Retorna uma lista de todos os reviews.

#### POST

Cria um novo review.

**Exemplo de Corpo de Requisição (POST):**

```json
{
    "stars": "Quantidade de estrelas para o filme",
    "comment": "Comentário para o filme",
    "movie": "Filme"
}
```

### Detalhar, Atualizar e Excluir Review

- **URL:** `/reviews/<int:pk>/`
- **Métodos Suportados:** `GET`, `PUT`, `DELETE`

#### GET

Retorna os detalhes de um review específico.

#### PUT

Atualiza os detalhes de um review específico.

**Exemplo de Corpo de Requisição (PUT):**

```json
{
    "stars": "Quantidade de estrelas para o filme atualizado",
    "comment": "Comentário para o filme

 atualizado",
    "movie": "Filme atualizado"
}
```

#### DELETE

Exclui um review específico.

**Resposta de Sucesso:**

```json
{
    "message": "Review deletado com sucesso."
}
```

**Resposta de Erro:**

```json
{
    "error": "Erro"
}
```

## Arquivos Importantes

### `reviews/views.py`

Contém as views para os endpoints da API:

- `ReviewCreateListView`: Gerencia requisições GET para listar reviews e POST para criar novos reviews.
- `ReviewRetrieveUpdateDestroyView`: Gerencia requisições GET para detalhar, PUT para atualizar e DELETE para excluir reviews específicos.

### `reviews/urls.py`

Define as rotas para os endpoints da API:

```python
from django.urls import path
from reviews.views import ReviewCreateListView, ReviewRetrieveUpdateDestroyView

urlpatterns = [
    path('reviews/', ReviewCreateListView.as_view(), name='review-create-list'),
    path('reviews/<int:pk>/', ReviewRetrieveUpdateDestroyView.as_view(), name='review-detail-view'),
]
```

## Licença

Este projeto está licenciado sob os termos da licença MIT.
