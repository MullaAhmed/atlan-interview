# using flask_restful
from flask import Flask, jsonify, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class RatingResponse(Resource):

    def get(self):
        message = {
        "Team":[ 
            {  
                "Name":"Minerva",
                "Member":"Ahmed",
                "Member":"Anmol",
                "Member":"Jay",
                "Member":"Anish:
            }
               ]
        }
        
        return jsonify(message)


api.add_resource(RatingResponse, '/')


# driver function
if __name__ == '__main__':

    app.run(debug=True)
