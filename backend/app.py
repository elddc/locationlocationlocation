from flask import Flask, request
from flask_cors import CORS

from location import Location
from power import power

api = Flask(__name__)
CORS(api)

@api.route('/locationlocationlocation')
def locationlocationlocation():
    latitude = float(request.args.get('lat'))
    longitude = float(request.args.get('lng'))
    radius = float(request.args.get('rad'))

    power_report = power(Location(latitude, longitude, radius))
    print(power_report.get_corn_power())

    response = {
        "Energy" : "Wind"
    }

    return response
