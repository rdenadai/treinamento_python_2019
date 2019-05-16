from starlette.applications import Starlette
from starlette.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles


application = Starlette(debug=True)
application.add_middleware(CORSMiddleware, allow_origins=["*"])
application.debug = True
application.mount("/static", StaticFiles(directory="src/static"))
