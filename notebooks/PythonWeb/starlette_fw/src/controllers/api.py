from starlette.responses import JSONResponse


def index(request):
    return JSONResponse({"id": "It Works"})
