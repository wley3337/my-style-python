"""empty message

Revision ID: 3799a9ee657e
Revises: 4df80323c479
Create Date: 2020-01-13 15:24:13.313513

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3799a9ee657e'
down_revision = '4df80323c479'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tags',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('worn',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('outfit_id', sa.Integer(), nullable=True),
    sa.Column('date_worn', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.ForeignKeyConstraint(['outfit_id'], ['outfits.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('clothing_categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.Column('clothing_item_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.ForeignKeyConstraint(['clothing_item_id'], ['clothing_items.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('clothing_tags',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tag_id', sa.Integer(), nullable=True),
    sa.Column('clothing_item_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.ForeignKeyConstraint(['clothing_item_id'], ['clothing_items.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tags.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('clothing_tags')
    op.drop_table('clothing_categories')
    op.drop_table('worn')
    op.drop_table('tags')
    op.drop_table('category')
    # ### end Alembic commands ###
