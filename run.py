from flask_blog_post import app

if __name__ == "__main__":
    app.run(
        debug=True
    )  # setting debug = True enables to make real-time changes to the project
    # without shutting down the flask_blog.py we can see changes on web by simply reloading the web page
