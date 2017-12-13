"""empty message

Revision ID: 221cddb2f017
Revises: 
Create Date: 2017-12-12 16:10:34.233138

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '221cddb2f017'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('likes_photo',
    sa.Column('photo_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['photo_id'], ['photos.photo_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('photo_id', 'user_id')
    )
    op.drop_constraint('likes_ibfk_2', 'likes', type_='foreignkey')
    op.drop_column('likes', 'photo_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('likes', sa.Column('photo_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.create_foreign_key('likes_ibfk_2', 'likes', 'photos', ['photo_id'], ['photo_id'])
    op.drop_table('likes_photo')
    # ### end Alembic commands ###