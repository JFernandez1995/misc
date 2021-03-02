from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class namingTest(Resource):
    def get(self,name,age,weight):
        return {name: {"age": age , "weight":weight}}

api.add_resource(namingTest, '/<string:name>/<int:age>/<int:weight>')

if __name__ == '__main__':
    app.run(debug=True)