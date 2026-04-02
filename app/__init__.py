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
    from app.routes.admin import bp as admin_bp
    from app.routes.main import bp as main_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(admin_bp)

    @app.errorhandler(404)
    def not_found(_e):
        return render_template("errors/404.html"), 404

    def _seed_issues() -> None:
        """Insert starter rows into `issues` when the table is empty."""
        from app.models.issue import Issue

        if Issue.query.count() > 0:
            click.echo("Reports already exist; seed skipped.")
            return
        starter_reports = [
            Issue(
                title="Streetlight out near Jinja Road junction (Nakawa)",
                category="lighting",
                area="Kampala Central",
                description=(
                    "The pole has been dark for several nights. Pedestrians and bodas struggle to see the crossing "
                    "after dusk."
                ),
                status="open",
            ),
            Issue(
                title="Deep pothole on Entebbe Road lane",
                category="streets",
                area="Entebbe",
                description=(
                    "Pothole growing wider after rain; vehicles swerve into oncoming traffic to avoid damage."
                ),
                status="in_progress",
            ),
            Issue(
                title="Overflowing waste bin near Old Taxi Park",
                category="sanitation",
                area="Nakasero",
                description=(
                    "Bin has been full for days; litter spreading onto the walkway. Resolved after extra collection run."
                ),
                status="resolved",
            ),
        ]
        db.session.add_all(starter_reports)
        db.session.commit()
        click.echo("Starter reports added successfully (3).")

    @app.cli.command("seed")
    def seed_command() -> None:
        """Load starter reports when the database is empty (optional; dev or staging)."""
        _seed_issues()

    @app.cli.command("seed-demo")
    def seed_demo_command() -> None:
        """Same as `flask seed` (kept for older notes that still say seed-demo)."""
        click.echo("Using flask seed — same command.")
        _seed_issues()

    return app
