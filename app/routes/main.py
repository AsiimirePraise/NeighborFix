from flask import (
    Blueprint,
    abort,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)

bp = Blueprint("main", __name__)

# UI-only sample rows (replaced by database in a later commit)
SAMPLE_ISSUES = [
    {
        "id": 1,
        "title": "Streetlight out — corner of Maple & 2nd",
        "category": "Lighting",
        "area": "Riverside",
        "status": "open",
        "updated": "Mar 28, 2026",
        "description": (
            "The pole-mounted fixture on the northeast corner has been dark for several nights. "
            "Pedestrian crossing is hard to see after dusk."
        ),
    },
    {
        "id": 2,
        "title": "Pothole widening eastbound lane",
        "category": "Streets & sidewalks",
        "area": "Downtown",
        "status": "in_progress",
        "updated": "Mar 27, 2026",
        "description": (
            "Roughly 12 inches across and getting deeper. Bikes swerve into traffic to avoid it."
        ),
    },
    {
        "id": 3,
        "title": "Overflowing public bin at bus stop",
        "category": "Sanitation",
        "area": "West End",
        "status": "resolved",
        "updated": "Mar 25, 2026",
        "description": (
            "Bin at stop ID 442 was full for days. Marked resolved after extra pickup scheduled."
        ),
    },
]

_ISSUES_BY_ID = {row["id"]: row for row in SAMPLE_ISSUES}


@bp.get("/")
def index():
    return render_template("index.html")


@bp.get("/issues")
def issues_list():
    return render_template("issues/list.html", issues=SAMPLE_ISSUES)


@bp.route("/issues/new", methods=["GET", "POST"])
def issues_new():
    if request.method == "POST":
        flash(
            "Thanks - your report was accepted for this demo. Saving to the database comes in the next commit.",
            "info",
        )
        return redirect(url_for("main.issues_list"))
    return render_template("issues/new.html")


@bp.get("/issues/<int:issue_id>")
def issue_detail(issue_id: int):
    issue = _ISSUES_BY_ID.get(issue_id)
    if issue is None:
        abort(404)
    return render_template("issues/detail.html", issue=issue)
