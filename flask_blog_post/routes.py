from flask import render_template, url_for, flash, redirect
from flask_blog_post import app
from flask_blog_post.forms import RegisterationForm, LoginForm


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
    # creating instance of register form, will be passed to register form html template
    form = RegisterationForm()
    # register method will receive post request also from register form
    # on clicking submit button and then after if block will be called
    if form.validate_on_submit():
        # on validation after submitting form on registration a flash message is generated
        # and redirecting to home page
        flash(message=f"Account created for {form.username.data}!", category="success")
        return redirect(url_for("home"))
    return render_template("register.html", title="Register", form=form)
    # passing form will give access to form variables


@app.route("/login", methods=["GET", "POST"])  # login page
def login():
    # creating instance of login form, will be passed to login form html template
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "test@gmail.com" and form.password.data == "password":
            flash(message="You have logged in!", category="success")
            return redirect(url_for("home"))
        else:
            flash("Login Unsuccesful, Please retry!", category="danger")
            # again load empty login page
    return render_template("login.html", title="Login", form=form)
    # passing form will give access to form variables
