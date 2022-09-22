from . import db 
from sqlalchemy.sql import func

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    post_title = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    # image = db.Column(db.Text, nullable=False)
    _category = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())