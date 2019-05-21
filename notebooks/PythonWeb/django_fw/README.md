## Django app

App esqueleto para a criaçao de projeto usando o framework Django.

## Executar o projeto

```bash
$> pip install requirements.txt
``` 

Se quiser criar o projeto do zero:

```bash
$> django-admin startproject exemplo
``` 

Antes de executar os comandos abaixo, é necessário ao menos definir um STATIC_ROOT no arquivo de **settings.py**.
Essa variável vaid definir em qual local do sistema operacional ficarão os arquivos estáticos do projeto.

```bash
$> python manage.py collectstatic # Coleta os arquivos estáticos e grava no diretório STATIC_ROOT
$> python manage.py makemigrations # Cria/Altera migrações de base de dados
$> python manage.py migrate # Migra (update) das migrações para o banco de dados
$> python manage.py createsuperuser # Cria um novo super usuário na base de dados do Django
``` 

```bash
$> gunicorn --reload --workers=3 -b 0.0.0.0:8585 exemplo.wsgi:application
``` 