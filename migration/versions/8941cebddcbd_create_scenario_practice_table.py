"""create scenario practice table

Revision ID: 8941cebddcbd
Revises: 2213b1428f72
Create Date: 2025-01-01 15:23:58.730137

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8941cebddcbd'
down_revision: Union[str, None] = '2213b1428f72'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'scenario_practices',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.id'), nullable=False),
        sa.Column('scenario_id', sa.Integer(), sa.ForeignKey('scenarios.id'), nullable=False),
        sa.Column('level1_time', sa.Integer(), nullable=False),
        sa.Column('level2_time', sa.Integer(), nullable=True),
        sa.Column('level3_time', sa.Integer(), nullable=True),
        sa.Column('finished_at', sa.DateTime(), nullable=False),
    )


def downgrade() -> None:
    pass
