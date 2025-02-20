"""create scenario element table

Revision ID: 161c6f6594e0
Revises: 0b707c183395
Create Date: 2025-01-01 15:22:41.873924

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '161c6f6594e0'
down_revision: Union[str, None] = '0b707c183395'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    scenario_elements_table = op.create_table(
        'scenario_elements',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('scenario_id', sa.Integer, sa.ForeignKey('scenarios.id'), nullable=False),
        sa.Column('level', sa.Integer, nullable=False),
        sa.Column('name', sa.String(50), nullable=False)
    )

    op.bulk_insert(
        scenario_elements_table,
        [
            {"scenario_id": 1, "level": 1, "name": "瑪格麗特披薩"},
            {"scenario_id": 1, "level": 2, "name": "臘腸披薩"},
            {"scenario_id": 1, "level": 3, "name": "燻雞披薩"},
        ],
    )


def downgrade() -> None:
    pass
