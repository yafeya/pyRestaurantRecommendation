from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from RestaurantApiControllers import RestaurantsAllApiController, RestaurantsInAreaApiController
from TestConnectionApiController import TestConnectionApiController
from werkzeug.serving import run_simple


app = Flask(__name__)
api = Api(app)
CORS(app)

app.config['SECRET_KEY'] = 'secret!'


def start_restful_server():
    ak = 'jLKWXCmDwGdfddhBvaB0GmqBr8K5gwum'
    sk = 'ZphXAtI0goU2aRcOGFpzPsWmZOY00UNa'
    print('starting restful server for restaurant recommendation...')
    restaurant_args = {'ak': ak, 'sk': sk}
    api.add_resource(RestaurantsInAreaApiController, '/restaurants/<location>/<price_section>',
                     resource_class_kwargs=restaurant_args)
    api.add_resource(TestConnectionApiController, '/test')
    app.run()

