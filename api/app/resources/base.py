import json
from flask import Response
from flask_restful import Resource

class BaseResource(Resource):
    def response(cls, data, status_code=200, 
                content_type='application/json', **kwargs):

        return Response(
            json.dumps(data, separators=(',', ': '), indent=4),
            status=status_code,
            content_type=content_type,
            **kwargs)