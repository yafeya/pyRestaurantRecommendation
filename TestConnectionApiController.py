from flask_restful import Resource


class TestConnectionApiController(Resource):

    def get(self):
        return 'You are connected', 200
