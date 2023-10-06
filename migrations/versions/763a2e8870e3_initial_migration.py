"""initial migration

Revision ID: 763a2e8870e3
Revises: 
Create Date: 2023-10-05 20:51:34.394995

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "763a2e8870e3"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # new genre table
    op.create_table(
        "genres",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )

    # genre id column to the books
    op.add_column("books", sa.Column("genre_id", sa.Integer(), nullable=True))

    # table for many to many relationship called book genre


def downgrade():
    pass
