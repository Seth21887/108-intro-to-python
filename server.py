import json #importing json will allow us to import lists through JSON notation
from flask import Flask
from about_me import me
from mock_data import catalog

app = Flask('Project')

@app.route("/", methods=["GET"]) #this is a decorator in python, the route will define an endpoint. the / means the root. The GET method means the user is trying to get something from the server
def home():
    return "This is the home page."

#Create an about endpoint and show your name
@app.route("/about", methods=["GET"]) #if no method is entered, by default it will be get.
def about():
    # return me["first"] + " " + me["last"]
    return f"{me['first' ]} {me['last']}"

@app.route("/myaddress")
def address():
    return f' {me["address"]["street"]} {me["address"]["number"]}' #this is a nested object

##########################################################################
##################### API ENDPOINTS #########################
################################################################
#Postman --> Tests endpoints of REST APIs

#the catalog that we are retrieving is just a python list of dictionaries.
@app.route("/api/catalog", methods=["GET"]) 
def get_catalog():
    return json.dumps(catalog) #the function dumps will convert some python object to json notation.

#make an endpoint to send back how many products we have in the catalog
@app.route("/api/catalog/count", methods=["GET"])
def get_count():
    #Here...count how many products are in the list catalog
    counts = len(catalog)

    return json.dumps(counts) #return the value

#Request 127.0.0.1:5000/api/product/1 (1 is the product _id here)
#instead of doing that for each product, it should be dynamic
#by using <id>, now anything we enter as the endpoint, will show up
@app.route("/api/product/<id>", methods=["GET"])
def get_product(id):
    return json.dumps(id)

app.run(debug=True)