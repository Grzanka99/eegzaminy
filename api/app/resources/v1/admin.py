from ..base import BaseResource
from flask_jwt_extended import jwt_required


class ProtectedResource(BaseResource):
    @jwt_required
    def get(self):
        return {'message': 'to je tajne'}
