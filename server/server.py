from flask import Flask, request, jsonify
import util
app = Flask(__name__)

@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_price', methods=['POST'])
def predict_price():
    sqm = float(request.form['sqm'])
    neighborhood = request.form['neighborhood']
    rooms = int(request.form['rooms'])
    bathrooms = int(request.form['bathrooms'])
    yob = float(request.form['yob'])
    heating = int(request.form['heating'])
    elevator = int(request.form['elevator'])

    response = jsonify({
        'estimated_price': util.get_price_estimate(neighborhood, rooms, sqm,
                                                   bathrooms, yob, heating, elevator)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    print("Starting Python Flask server")
    app.run()