"""admin_users table

Revision ID: b2f8a1c3d4e5
Revises: 91ecda23494f
Create Date: 2026-04-02

"""
from alembic import op
import sqlalchemy as sa


revision = "b2f8a1c3d4e5"
down_revision = "91ecda23494f"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "admin_users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("username", sa.String(length=80), nullable=False),
        sa.Column("password_hash", sa.String(length=256), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    with op.batch_alter_table("admin_users", schema=None) as batch_op:
        batch_op.create_index(batch_op.f("ix_admin_users_username"), ["username"], unique=True)


def downgrade():
    with op.batch_alter_table("admin_users", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_admin_users_username"))
    op.drop_table("admin_users")
