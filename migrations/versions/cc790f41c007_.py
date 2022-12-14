"""empty message

Revision ID: cc790f41c007
Revises: c4bec2a547f6
Create Date: 2022-11-30 16:04:51.934129

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cc790f41c007'
down_revision = 'c4bec2a547f6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('board')
    op.drop_table('task')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('task',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('body', sa.VARCHAR(length=140), nullable=False),
    sa.Column('status', sa.BOOLEAN(), nullable=True),
    sa.Column('created_on', sa.DATETIME(), nullable=True),
    sa.Column('updated_on', sa.DATETIME(), nullable=True),
    sa.Column('board_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['board_id'], ['board.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('body')
    )
    op.create_table('board',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('status', sa.VARCHAR(length=8), nullable=False),
    sa.Column('created_on', sa.DATETIME(), nullable=True),
    sa.Column('updated_on', sa.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
