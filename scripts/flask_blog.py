from flask import Flask
app = Flask(__name__) # __name__ can be replaced by __main__ if python is used to call this script

@app.route("/") # root page
def hello():
    return "<h1>hello world</h1>"

if __name__ == "__main__":
    app.run(debug=True) # setting debug = True enables to make real-time changes to the project
    # without shutting down the flask_blog.py we can see changes on web by simply reloading the web page
