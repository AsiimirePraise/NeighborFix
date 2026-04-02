"""Staff routes: sign in with DB accounts, triage issue status."""

from __future__ import annotations

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
from app.models.admin_user import AdminUser
from app.models.issue import Issue

bp = Blueprint("admin", __name__, url_prefix="/admin")

ALLOWED_STATUS = frozenset({"open", "in_progress", "resolved"})


def _admin_users_exist() -> bool:
    return AdminUser.query.count() > 0


@bp.before_request
def _guard_admin():
    if request.endpoint in ("admin.login", "admin.logout"):
        return None
    if not _admin_users_exist():
        return redirect(url_for("admin.login"))
    if not session.get("admin_user_id"):
        return redirect(url_for("admin.login", next=request.path))


@bp.route("/login", methods=["GET", "POST"])
def login():
    if not _admin_users_exist():
        return render_template(
            "admin/disabled.html",
            message="No staff accounts yet. Run database migrations, then run: flask seed (creates default admins).",
        )

    if session.get("admin_user_id"):
        return redirect(url_for("admin.dashboard"))

    error = None
    if request.method == "POST":
        username = (request.form.get("username") or "").strip()
        password = request.form.get("password") or ""
        user = AdminUser.query.filter_by(username=username).first()
        if user and user.check_password(password):
            session["admin_user_id"] = user.id
            session["admin_username"] = user.username
            session.permanent = True
            nxt = (request.form.get("next") or request.args.get("next") or "").strip()
            if not nxt.startswith("/"):
                nxt = url_for("admin.dashboard")
            return redirect(nxt)
        error = "Incorrect username or password."

    return render_template("admin/login.html", error=error)


@bp.route("/logout", methods=["GET", "POST"])
def logout():
    session.pop("admin_user_id", None)
    session.pop("admin_username", None)
    session.pop("admin_logged_in", None)
    return redirect(url_for("main.index"))


@bp.route("/")
@bp.route("")
def dashboard():
    issues = Issue.query.order_by(Issue.updated_at.desc()).all()
    return render_template(
        "admin/dashboard.html",
        issues=issues,
        staff_name=session.get("admin_username"),
    )


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
