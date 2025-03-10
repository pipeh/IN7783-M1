from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_URL = "/docs"
API_URL = "/static/swagger.yaml"


def create_app():
    app = Flask(__name__)

    # Register blueprints (modular endpoints)
    from .routes.home import main as home
    from .routes.profile import main as profile
    app.register_blueprint(home)
    app.register_blueprint(profile)

    swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL)
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

    return app