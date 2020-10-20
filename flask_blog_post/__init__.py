from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(
    __name__
)  # __name__ can be replaced by __main__ if python is used to call this script

# secret key created using python build-in secrets module
app.config["SECRET_KEY"] = "f660a471446ab1694afc64df9f83991a"
# setting db path, 3 forward slash indicates relative path
# sqlite db is used, sqlalchemy is used to work or query sqlite db
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
# sqlalchemy db instance
db = SQLAlchemy(app)
# hashing method
bcrypt = Bcrypt(app)

from flask_blog_post import routes
