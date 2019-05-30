import json
from flask import Flask, request, jsonify
from flask_restful import Api
from flask_cors import CORS
from RestaurantApiControllers import RestaurantsInAreaApiController


app = Flask(__name__)
api = Api(app)
CORS(app)

app.config['SECRET_KEY'] = 'secret!'
app.config['JSON_AS_ASCII'] = False
ak = 'jLKWXCmDwGdfddhBvaB0GmqBr8K5gwum'
sk = 'ZphXAtI0goU2aRcOGFpzPsWmZOY00UNa'
__restaurant_api__ = RestaurantsInAreaApiController(ak=ak, sk=sk)


@app.route('/')
def index():
    data = {'payload': 'Welcome to Restaurants Service', 'list': ['str1', 'str2']}
    return jsonify(data), 200


@app.route('/restaurants', methods=['GET'])
def restaurants():
    location = request.args.get('location')
    price_section = request.args.get('price')
    return __restaurant_api__.get(location, price_section)


if __name__ == '__main__':
    app.run()
