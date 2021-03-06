"""empty message

Revision ID: e13763c4af95
Revises: 
Create Date: 2017-12-13 16:30:52.105558

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e13763c4af95'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('messages',
    sa.Column('message_id', sa.Integer(), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.Column('chat_id', sa.Integer(), nullable=True),
    sa.Column('text', sa.String(length=400), nullable=True),
    sa.Column('date', sa.String(length=50), nullable=True),
    sa.Column('read', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['users.user_id'], ),
    sa.ForeignKeyConstraint(['chat_id'], ['chat.chat_id'], ),
    sa.PrimaryKeyConstraint('message_id')
    )
    op.drop_table('likes_photo')
    op.drop_table('massages')
    op.add_column('chat', sa.Column('first_member_id', sa.Integer(), nullable=True))
    op.add_column('chat', sa.Column('last_message_id', sa.Integer(), nullable=True))
    op.add_column('chat', sa.Column('second_member_id', sa.Integer(), nullable=True))
    op.drop_constraint('chat_ibfk_1', 'chat', type_='foreignkey')
    op.create_foreign_key(None, 'chat', 'users', ['first_member_id'], ['user_id'])
    op.create_foreign_key(None, 'chat', 'messages', ['last_message_id'], ['message_id'])
    op.create_foreign_key(None, 'chat', 'users', ['second_member_id'], ['user_id'])
    op.drop_column('chat', 'chat_name')
    op.drop_column('chat', 'member')
    op.add_column('likes', sa.Column('photo_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'likes', 'photos', ['photo_id'], ['photo_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'likes', type_='foreignkey')
    op.drop_column('likes', 'photo_id')
    op.add_column('chat', sa.Column('member', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))
    op.add_column('chat', sa.Column('chat_name', mysql.VARCHAR(collation='utf8_unicode_ci', length=150), nullable=True))
    op.drop_constraint(None, 'chat', type_='foreignkey')
    op.drop_constraint(None, 'chat', type_='foreignkey')
    op.drop_constraint(None, 'chat', type_='foreignkey')
    op.create_foreign_key('chat_ibfk_1', 'chat', 'users', ['member'], ['user_id'])
    op.drop_column('chat', 'second_member_id')
    op.drop_column('chat', 'last_message_id')
    op.drop_column('chat', 'first_member_id')
    op.create_table('massages',
    sa.Column('massage_id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('author_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('chat_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('text', mysql.TEXT(collation='utf8_unicode_ci'), nullable=True),
    sa.Column('date', mysql.VARCHAR(collation='utf8_unicode_ci', length=50), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['users.user_id'], name='massages_ibfk_1'),
    sa.ForeignKeyConstraint(['chat_id'], ['chat.chat_id'], name='massages_ibfk_2'),
    sa.PrimaryKeyConstraint('massage_id'),
    mysql_collate='utf8_unicode_ci',
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('likes_photo',
    sa.Column('photo_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('user_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['photo_id'], ['photos.photo_id'], name='likes_photo_ibfk_1'),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], name='likes_photo_ibfk_2'),
    sa.PrimaryKeyConstraint('photo_id', 'user_id'),
    mysql_collate='utf8_unicode_ci',
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.drop_table('messages')
    # ### end Alembic commands ###
