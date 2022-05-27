from flask import Flask

app = Flask('Project')

@app.route("/", methods=["GET"]) #this is a decorator in python, the route will define an endpoint. the / means the root. The GET method means the user is trying to get something from the server
def home():
    return "This is the home page."

#Create an about endpoint and show your name
@app.route("/about", methods=["GET"]) #if no method is entered, by default it will be get.
def about():
    me = {
    "first": "Seth",
    "last": "LaFountain",
    "age": 35
    }
    return(me)

app.run(debug=True)