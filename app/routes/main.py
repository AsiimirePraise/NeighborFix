from flask import (
    Blueprint,
    abort,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)

from app.extensions import db
from app.models.issue import Issue

bp = Blueprint("main", __name__)


@bp.get("/")
def index():
    return render_template("index.html")


@bp.get("/issues")
def issues_list():
    issues = Issue.query.order_by(Issue.updated_at.desc()).all()
    return render_template("issues/list.html", issues=issues)


@bp.route("/issues/new", methods=["GET", "POST"])
def issues_new():
    if request.method == "POST":
        title = (request.form.get("title") or "").strip()
        category = (request.form.get("category") or "").strip()
        area = (request.form.get("area") or "").strip()
        description = (request.form.get("description") or "").strip()
        if not title or not category or not area or not description:
            flash("Please fill in all fields.", "error")
            return render_template("issues/new.html"), 400
        issue = Issue(
            title=title[:120],
            category=category[:40],
            area=area[:80],
            description=description[:2000],
            status="open",
        )
        db.session.add(issue)
        db.session.commit()
        return redirect(url_for("main.issue_detail", issue_id=issue.id, saved=1))
    return render_template("issues/new.html")


@bp.get("/issues/<int:issue_id>")
def issue_detail(issue_id: int):
    issue = db.session.get(Issue, issue_id)
    if issue is None:
        abort(404)
    return render_template(
        "issues/detail.html",
        issue=issue,
        just_saved=request.args.get("saved") == "1",
    )
