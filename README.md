# School API

## Objetivo do sistema
* API que seja capaz de armazenar dados de estudantes no sistema;
* Criar endpoints para: criar, listar, alterar, remover e filtrar estudantes.

## Instalação em ambiente de desenvolvimento

### Pré-requisitos
Ter instalado as versões mais recentes da linguagem [Python](https://www.python.org/downloads/) e da ferramenta [docker-compose](https://docs.docker.com/compose/install/).

Obs: Usaremos o docker-compose para subir um container com um banco PostgreSQL para desenvolvimento.

1. Criar um ambiente virtual para isolar as dependências que instalaremos

    ```bash
    $ python -m venv .venv --prompt school_api
    ```

2. Ativar o ambiente criado

    No Linux
    ```bash
    $ source .venv/bin/activate
    ```

    Informações sobre ativação em outros Sistemas Operacionais podem ser conferidas em: https://docs.python.org/pt-br/3/library/venv.html


3. Instalar as dependências do sistema

    ```bash
    $ pip install -r requirements.txt
    ```

4. Subir o container com o banco de dados

    ```bash
    $ docker-compose up -d
    ```

5. Executar as migrações para criar toda a estrutura do banco de dados

    ```bash
    $ python manage.py migrate
    ```

6. Rodar o sistema

    ```bash
    $ python manage.py runserver
    ```
    A aplicação estará disponível em: http://localhost:8000/
