from __future__ import annotations

from datetime import datetime, timezone

from sqlalchemy import event, func

from app.constants import CATEGORY_IMAGE_URLS, CATEGORY_LABELS
from app.extensions import db


class Issue(db.Model):
    __tablename__ = "issues"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    category = db.Column(db.String(40), nullable=False, index=True)
    area = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), nullable=False, default="open", index=True)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = db.Column(
        db.DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    @property
    def category_display(self) -> str:
        return CATEGORY_LABELS.get(self.category, self.category.replace("_", " ").title())

    @property
    def category_image_url(self) -> str:
        return CATEGORY_IMAGE_URLS.get(
            self.category,
            CATEGORY_IMAGE_URLS["other"],
        )

    def _format_dt(self, dt: datetime | None) -> str:
        if dt is None:
            return ""
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.strftime("%b %d, %Y")

    @property
    def created_display(self) -> str:
        return self._format_dt(self.created_at)

    @property
    def updated_display(self) -> str:
        return self._format_dt(self.updated_at)


@event.listens_for(Issue, "before_update", propagate=True)
def _issue_touch_updated(_mapper, _connection, target: Issue) -> None:
    target.updated_at = datetime.now(timezone.utc)
