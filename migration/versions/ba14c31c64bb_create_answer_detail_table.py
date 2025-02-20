"""create answer detail  table

Revision ID: ba14c31c64bb
Revises: 8941cebddcbd
Create Date: 2025-01-01 15:58:25.897002

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ba14c31c64bb'
down_revision: Union[str, None] = '8941cebddcbd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'answer_details',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('record_id', sa.Integer, index=True, nullable=False),
        sa.Column('question_id', sa.Integer, sa.ForeignKey("questions.id"), nullable=False),
        sa.Column('question_type', sa.String(50), nullable=False),
        sa.Column('level', sa.Integer, nullable=False),
        sa.Column('selected_mixed_number', sa.Integer, nullable=True),
        sa.Column('selected_numerator', sa.Integer, nullable=True),
        sa.Column('selected_denominator', sa.Integer, nullable=True),
        sa.Column('selected_operator', sa.String(2), nullable=True),
    )


def downgrade() -> None:
    pass
