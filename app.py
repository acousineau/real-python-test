# import the Flask class from the flask package
from flask import Flask

# create the application object
app = Flask(__name__)

# error handling
app.config["DEBUG"] = True

# use the decorator pattern to
# link the view function to a url
@app.route("/")
@app.route("/hello")
# define the view using a function, which returns a string
def hello_world():
    return "Hello, world!"

# dynamic route
@app.route("/test/<search_query>")
def search(search_query):
    return search_query

# different value type paths
@app.route("/integer/<int:value>")
def int_type(value):
    print(value + 1)
    return "integer"

@app.route("/float/<float:value>")
def float_type(value):
    print(value + 1)
    return "float"

@app.route("/path/<path:value>")
def path_type(value):
    print(value)
    return "path"

@app.route("/name/<name>")
def index(name):
    if name.lower() == "michael":
        return "Hello, {}".format(name)
    else:
        return "Not Found", 404

# start the development server using the run() method
if __name__ == "__main__":
    app.run()