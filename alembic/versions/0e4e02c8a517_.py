"""empty message

Revision ID: 0e4e02c8a517
Revises: 61b9825388f1
Create Date: 2025-08-09 02:16:00.912414

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0e4e02c8a517'
down_revision: Union[str, Sequence[str], None] = '61b9825388f1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
