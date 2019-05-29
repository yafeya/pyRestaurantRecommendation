from flask_restful import Resource


class TestConnectionApiController(Resource):
    def get(self):
        return 'You are connected', 200


class IndexConnectionApiController(Resource):
    def get(self):
        return 'Restaurant Service', 200
