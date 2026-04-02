"""Staff-only routes to triage reports (open / in progress / resolved)."""

from __future__ import annotations

import os

from flask import (
    Blueprint,
    abort,
    redirect,
    render_template,
    request,
    session,
    url_for,
)

from app.extensions import db
from app.models.issue import Issue

bp = Blueprint("admin", __name__, url_prefix="/admin")

ALLOWED_STATUS = frozenset({"open", "in_progress", "resolved"})


def _admin_password_configured() -> bool:
    return bool(os.environ.get("ADMIN_PASSWORD", "").strip())


def _password_ok(pw: str | None) -> bool:
    expected = os.environ.get("ADMIN_PASSWORD", "")
    if not expected.strip():
        return False
    return (pw or "") == expected


@bp.before_request
def _guard_admin():
    if request.endpoint in ("admin.login", "admin.logout"):
        return None
    if not _admin_password_configured():
        return redirect(url_for("admin.login"))
    if not session.get("admin_logged_in"):
        return redirect(url_for("admin.login", next=request.path))


@bp.route("/login", methods=["GET", "POST"])
def login():
    if not _admin_password_configured():
        return render_template(
            "admin/disabled.html",
            message="Set ADMIN_PASSWORD in your .env file, restart the app, then return here.",
        )

    if session.get("admin_logged_in"):
        return redirect(url_for("admin.dashboard"))

    error = None
    if request.method == "POST":
        if _password_ok(request.form.get("password")):
            session["admin_logged_in"] = True
            session.permanent = True
            nxt = (request.form.get("next") or request.args.get("next") or "").strip()
            if not nxt.startswith("/"):
                nxt = url_for("admin.dashboard")
            return redirect(nxt)
        error = "Incorrect password."

    return render_template("admin/login.html", error=error)


@bp.route("/logout", methods=["GET", "POST"])
def logout():
    session.pop("admin_logged_in", None)
    return redirect(url_for("main.index"))


@bp.route("/")
def dashboard():
    issues = Issue.query.order_by(Issue.updated_at.desc()).all()
    return render_template("admin/dashboard.html", issues=issues)


@bp.post("/issues/<int:issue_id>/status")
def issue_status(issue_id: int):
    issue = db.session.get(Issue, issue_id)
    if issue is None:
        abort(404)
    status = (request.form.get("status") or "").strip()
    if status not in ALLOWED_STATUS:
        return redirect(url_for("admin.dashboard"))
    issue.status = status
    db.session.commit()
    return redirect(url_for("admin.dashboard"))
