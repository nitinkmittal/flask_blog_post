from flask import render_template, url_for, flash, redirect, request
from flask_blog_post import app, db, bcrypt
from flask_blog_post.forms import RegisterationForm, LoginForm
from flask_blog_post.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required

posts = [
    {
        "author": "Nitin Kumar Mittal",
        "title": "First Flask App",
        "content": "This is my first app",
        "date": "September 17, 2020",
    },
    {
        "author": "Tanvi Tembhurne",
        "title": "First Job",
        "content": "This is about my first job",
        "date": "September 17, 2020",
    },
]


@app.route("/")  # root page
@app.route("/home")  # multiple decorators can be used to get to same web page
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")  # about page
def about():
    return render_template("about.html", title="About")


@app.route("/register", methods=["GET", "POST"])  # register page
def register():
    # if user is already logged in then no need to show login form again
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    # creating instance of register form, will be passed to register form html template
    form = RegisterationForm()
    # register method will receive post request also from register form
    # on clicking submit button and then after if block will be called
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode(
            "utf-8"
        )
        user = User(
            username=form.username.data, email=form.email.data, password=hashed_password
        )
        db.session.add(user)
        db.session.commit()
        # on validation after submitting form on registration a flash message is generated
        # and redirecting to home page
        flash(
            message=f"Account has been created for {form.username.data}!",
            category="success",
        )
        return redirect(url_for("login"))
    return render_template("register.html", title="Register", form=form)
    # passing form will give access to form variables


@app.route("/login", methods=["GET", "POST"])  # login page
def login():
    # if user is already logged in then no need to show login form again
    if current_user.is_authenticated:
        return redirect(url_for("home"))

    # creating instance of login form, will be passed to login form html template
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            # maintaing logged user session using login_user functionality from flask_login
            login_user(user=user, remember=form.remember.data)

            # return to requested page
            next_page_url = request.args.get("next")
            return (
                redirect(next_page_url) if next_page_url else redirect(url_for("home"))
            )
        flash("Login Unsuccesful, Please check email and password!", category="danger")
        # again load empty login page

    return render_template("login.html", title="Login", form=form)
    # passing form will give access to form variables


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route("/account")
@login_required  # enables account link to be accessible only if already login
def account():
    image_file = url_for("static", filename="images/" + "current_user.image_file")
    return render_template("account.html", title="Account")
