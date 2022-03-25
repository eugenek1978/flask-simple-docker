from flask import Flask
from flask_restful import abort, Resource, Api

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return 'Hello world'

class HelloWorldWithName(Resource):
    def get(self, name):
        if name == 'Yevgeniy':
            abort(404, message='Hello exception')
        return 'Hello ' + name + ' !!!'

##
## Actually setup the Api resource routing here
##
api.add_resource(HelloWorld, '/')
api.add_resource(HelloWorldWithName, '/<name>')

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')