#! /var/mail/flask
from flask import Flask
#, request
from flask_restful import Resource, Api
#, abort, reqparse

# this wraps our app in an api and this initializes a restful api
app = Flask(__name__)
api = Api(app)

# make a resource in this api, named HelloWorld 
# overridden the get method i.e. this is what will happen when send a get request to a specific url
# when that happens, we will return Hello World!
class HelloWorld(Resource):
    def get(self, name, test):
        return {"name": name, "test": test}
# now need to register this as a resource api.add_resource(Class, url) (can use a / to use a default url)
# essentially, it determines what the root of the resource will be
api.add_resource(HelloWorld, "/helloworld/<string:name>/<int:test>")

# this starts both the server and the application
# debug=True says that we are in debug mode so we will see all of that output and any logging information, so if we have a bug it will tell us why
if __name__ == "__main__":
    app.run(debug=True)