from flask import Flask, render_template

app = Flask(
    __name__
)  # __name__ can be replaced by __main__ if python is used to call this script

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


@app.route("/about")  # root page
def about():
    return render_template("about.html", title="About")


if __name__ == "__main__":
    app.run(
        debug=True
    )  # setting debug = True enables to make real-time changes to the project
    # without shutting down the flask_blog.py we can see changes on web by simply reloading the web page
