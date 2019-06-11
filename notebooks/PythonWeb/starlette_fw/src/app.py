import os
from starlette.applications import Starlette
from starlette.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles
from starlette.routing import Mount, Route, Router
from .controllers.principal import documentation
from .controllers.api import index


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


router = Router(
    [
        Route("/", endpoint=documentation, methods=["GET"]),
        Route("/api/", endpoint=index, methods=["GET"]),
    ]
)

application = Starlette(debug=True)
application.add_middleware(CORSMiddleware, allow_origins=["*"])
application.mount("/static", StaticFiles(directory=f"{BASE_DIR}/src/static"))
application.mount("", router)
