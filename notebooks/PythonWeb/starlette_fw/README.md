## Starlette / uvicorn app

App esqueleto para a criaçao de projeto usando o framework Starlette com uvicorn.

## Executar o projeto

```bash
$> pip install requirements.txt
$> gunicorn -w 4 -k uvicorn.workers.UvicornWorker --reload -b 0.0.0.0:8585 asgi:application
```