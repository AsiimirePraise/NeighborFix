from flask import Flask


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_prefixed_env()

    from app.routes.main import bp as main_bp

    app.register_blueprint(main_bp)

    return app
