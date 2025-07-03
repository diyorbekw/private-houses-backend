"""Delete exam form

Revision ID: da78aeaaf65d
Revises: d6879874a66c
Create Date: 2025-07-03 15:50:48.500235
"""

from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'da78aeaaf65d'
down_revision: Union[str, Sequence[str], None] = 'd6879874a66c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # First, drop the foreign key constraint from study_info to exam_forms
    op.drop_constraint(op.f('study_info_exam_form_id_fkey'), 'study_info', type_='foreignkey')

    # Then drop the exam_form_id column from study_info
    op.drop_column('study_info', 'exam_form_id')

    # Finally, drop the exam_forms table
    op.drop_table('exam_forms')


def downgrade() -> None:
    """Downgrade schema."""
    # Recreate exam_forms table
    op.create_table(
        'exam_forms',
        sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column('name', sa.VARCHAR(), nullable=False),
        sa.PrimaryKeyConstraint('id', name=op.f('exam_forms_pkey')),
        sa.UniqueConstraint(
            'name',
            name=op.f('exam_forms_name_key'),
            postgresql_include=[],
            postgresql_nulls_not_distinct=False
        )
    )

    # Add exam_form_id column back to study_info
    op.add_column('study_info', sa.Column('exam_form_id', sa.INTEGER(), nullable=False))

    # Restore the foreign key constraint
    op.create_foreign_key(
        op.f('study_info_exam_form_id_fkey'),
        'study_info',
        'exam_forms',
        ['exam_form_id'],
        ['id']
    )
