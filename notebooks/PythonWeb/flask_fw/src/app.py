import os

from flask import Flask
from flask_cors import CORS
from flask_assets import Environment, Bundle
from .controllers.principal import principal
from .controllers.api import api
from .settings import Config


# Start the flask app | Correcting CORS
application = Flask(__name__)
application.secret_key = (
    b"flaskvl^qk#q^ml3v=0lk*b@^88b))hb17u@zj^m#!t#u%rlj$96r_wpython"
)

cors = CORS(application, resources={r"/*": {"origins": "*"}})

# Assets
# ---------------
assets = Environment()
js = Bundle("js/default.js", filters="jsmin", output="gen/packed.js")
css = Bundle("css/default.css", output="gen/packed.css")
assets.register("js_all", js)
assets.register("css_all", css)
assets.init_app(application)

# Configuration
# ---------------
application.config.from_object(Config())

# Controllers
# ---------------
# Register the apps blueprint endpoints
application.register_blueprint(principal)
application.register_blueprint(api)
