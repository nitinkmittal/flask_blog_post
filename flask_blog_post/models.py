from datetime import datetime
from flask_blog_post import db, login_manager
from flask_login import UserMixin


# to manage user session
@login_manager.user_loader
def load_user(user_id):
    # will return user for that particular user_id
    # User.query.get(int(user_id)) capability given by UserMixin
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    # inheriting UserMixin class will enablle maintaining user_id for a user
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(120), nullable=False, default="default.jpg")
    password = db.Column(db.String(60), nullable=False)
    # posts is not actually a column but a dynamically query column
    # backref column will be accessed through Post table
    posts = db.relationship("Post", backref="author", lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    # creating user's id as foreign key
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}',)"
