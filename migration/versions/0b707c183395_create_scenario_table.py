"""create scenario table

Revision ID: 0b707c183395
Revises: 
Create Date: 2025-01-01 15:16:33.946917

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0b707c183395'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    scenarios_table = op.create_table(
        "scenarios",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("name", sa.String(50), nullable=False),
    )

    op.bulk_insert(
        scenarios_table,
        [
            {"name": "賣披薩"},
        ],
    )


def downgrade() -> None:
    pass
