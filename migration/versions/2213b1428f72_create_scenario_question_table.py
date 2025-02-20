"""create scenario question table

Revision ID: 2213b1428f72
Revises: 161c6f6594e0
Create Date: 2025-01-01 15:23:46.539143

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2213b1428f72'
down_revision: Union[str, None] = '161c6f6594e0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    scenario_question_table = op.create_table(
        'scenario_questions',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('scenario_element_id', sa.Integer(), sa.ForeignKey(
            'scenario_elements.id'), nullable=False),
        sa.Column('mixed_number', sa.Integer(), nullable=True),
        sa.Column('numerator', sa.Integer(), nullable=True),
        sa.Column('denominator', sa.Integer(), nullable=True),
    )

    question_list = []
    denominators = [4, 6, 8, 12]
    for scenario_element_id in range(1, 4):
        for denominator in denominators:
            scenario_question = {
                'scenario_element_id': scenario_element_id,
                'mixed_number': 1,
                'numerator': None,
                'denominator': None
            }
            question_list.append(scenario_question)
            for numerator in range(1, denominator):
                scenario_question = {
                    'scenario_element_id': scenario_element_id,
                    'mixed_number': None,
                    'numerator': numerator,
                    'denominator': denominator
                }
                question_list.append(scenario_question)

    op.bulk_insert(scenario_question_table, question_list)
def downgrade() -> None:
    pass
