import os

from flask import Flask
from flask_cors import CORS
from flask_assets import Environment, Bundle
from .controllers.principal import principal
from .controllers.api import api
from .settings import Config


# Start the flask app | Correcting CORS
application = Flask(__name__)
cors = CORS(application, resources={r"/*": {"origins": "*"}})

# Assets
# ---------------
# assets = Environment()
# js = Bundle("js/default.js", filters="jsmin", output="gen/packed.js")
# css = Bundle("css/default.css", output="gen/packed.css")
# assets.register("js_all", js)
# assets.register("css_all", css)
# assets.init_app(application)

# Configuration
# ---------------
application.config.from_object(Confg())

# Controllers
# ---------------
# Register the apps blueprint endpoints
application.register_blueprint(principal)
application.register_blueprint(api)
