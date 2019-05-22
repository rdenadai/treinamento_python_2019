## Flask app

App esqueleto para a criaçao de projeto usando o framework Flask.

## Executar o projeto

```bash
$> pip install requirements.txt
$> gunicorn wsgi --workers=3 --reload -b 0.0.0.0:8585
``` 

## Referências

 - [Flask](http://flask.pocoo.org/)
 - [Modular Applications with Blueprints](http://flask.pocoo.org/docs/1.0/blueprints/)
 - [wsgi](https://www.python.org/dev/peps/pep-3333/)
 - [gunicorn](https://gunicorn.org/)
 