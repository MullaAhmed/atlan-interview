# using flask_restful
from flask import Flask, jsonify, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class RatingResponse(Resource):

    def get(self):
        message = {
    "Teams": [
      {
        "Minerva": 
        [
          {
            "Member 1": "Ahmed",
            "Member 2": "Anmol",
            "Member 3": "Jay",
            "Member 4": "Anish",
          }
        ],
        
        "Manentia":
        [ 
          {
            "Member 1": "Anuj",
            "Member 2": "Hitesh",
            "Member 3": "Jitender",
            "Member 4": "Chand",
          }
         ] ,
          
      }
      ]}
        
        return jsonify(message)


api.add_resource(RatingResponse, '/')


# driver function
if __name__ == '__main__':
  app.run(debug=True)
