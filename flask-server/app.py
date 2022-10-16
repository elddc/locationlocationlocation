from flask import Flask, request
from flask_cors import CORS

api = Flask(__name__)
CORS(api)

@api.route('/locationlocationlocation')
def locationlocationlocation():
    print(request.args)
    response = {
        "Energy" : "Wind"
    }

    return response
