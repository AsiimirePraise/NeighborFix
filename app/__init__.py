import os

from flask import Flask, render_template


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_prefixed_env()
    # Flash/session need a non-empty secret; env wins for production.
    app.config["SECRET_KEY"] = (
        os.environ.get("SECRET_KEY")
        or app.config.get("SECRET_KEY")
        or "dev-secret-key-change-with-env-in-production"
    )

    from app.routes.main import bp as main_bp

    app.register_blueprint(main_bp)

    @app.errorhandler(404)
    def not_found(_e):
        return render_template("errors/404.html"), 404

    return app
