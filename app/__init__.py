import os

import click
from flask import Flask, render_template

from app.extensions import db, migrate


def _database_uri(app: Flask) -> str:
    uri = os.environ.get("DATABASE_URL")
    if uri:
        if uri.startswith("postgres://"):
            uri = uri.replace("postgres://", "postgresql://", 1)
        return uri
    return "sqlite:///" + os.path.join(app.instance_path, "neighborfix.db")


def create_app() -> Flask:
    app = Flask(__name__, instance_relative_config=True)
    os.makedirs(app.instance_path, exist_ok=True)
    app.config.from_prefixed_env()
    app.config["SECRET_KEY"] = (
        os.environ.get("SECRET_KEY")
        or app.config.get("SECRET_KEY")
        or "dev-secret-key-change-with-env-in-production"
    )
    app.config["SQLALCHEMY_DATABASE_URI"] = _database_uri(app)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    migrate.init_app(app, db)

    from app import models  # noqa: F401 — register models with SQLAlchemy
    from app.routes.main import bp as main_bp

    app.register_blueprint(main_bp)

    @app.errorhandler(404)
    def not_found(_e):
        return render_template("errors/404.html"), 404

    @app.cli.command("seed")
    def seed() -> None:
        """Load starter reports when the database is empty (optional; dev or staging)."""
        from app.models.issue import Issue

        if Issue.query.count() > 0:
            click.echo("Reports already exist; seed skipped.")
            return
        starter_reports = [
            Issue(
                title="Streetlight out — corner of Maple & 2nd",
                category="lighting",
                area="Riverside",
                description=(
                    "The pole-mounted fixture on the northeast corner has been dark for several nights. "
                    "Pedestrian crossing is hard to see after dusk."
                ),
                status="open",
            ),
            Issue(
                title="Pothole widening eastbound lane",
                category="streets",
                area="Downtown",
                description=(
                    "Roughly 12 inches across and getting deeper. Bikes swerve into traffic to avoid it."
                ),
                status="in_progress",
            ),
            Issue(
                title="Overflowing public bin at bus stop",
                category="sanitation",
                area="West End",
                description=(
                    "Bin at stop ID 442 was full for days. Marked resolved after extra pickup scheduled."
                ),
                status="resolved",
            ),
        ]
        db.session.add_all(starter_reports)
        db.session.commit()
        click.echo("Starter reports added successfully (3).")

    return app
