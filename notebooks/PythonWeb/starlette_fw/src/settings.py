import os
from starlette.templating import Jinja2Templates


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

templates = Jinja2Templates(directory=f"{BASE_DIR}/src/templates")
