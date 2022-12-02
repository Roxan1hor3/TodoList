"""empty message

Revision ID: 3245e5732fc1
Revises: 8f854d3672dd
Create Date: 2022-11-30 19:00:57.332430

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3245e5732fc1'
down_revision = '8f854d3672dd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('task')
    op.drop_table('board')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('board',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('status', sa.VARCHAR(length=8), nullable=False),
    sa.Column('created_on', sa.DATETIME(), nullable=True),
    sa.Column('updated_on', sa.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
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
    # ### end Alembic commands ###
