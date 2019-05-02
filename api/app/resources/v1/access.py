from ..base import BaseResource
from ...models import UserModel, RevokedTokenModel
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    jwt_refresh_token_required,
    get_jwt_identity,
    get_raw_jwt
)
from flask_restful import reqparse


parser = reqparse.RequestParser()
parser.add_argument('username', help='This field cannot be blank', required=True)
parser.add_argument('password', help='This field cannot be blank', required=True)


class UserRegistration(BaseResource):
    def post(self):
        data = parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return self.response(
                {'message': 'User {} already exists'.format(data['username'])}, 409
            )

        new_user = UserModel(
            username=data['username'],
            password=UserModel.generate_hash(data['password'])
        )

        try:
            new_user.add_user()
            access_token = create_access_token(identity=data['username'])
            refresh_token = create_refresh_token(identity=data['username'])
            return self.response(
                {
                    'message': 'User {} was created'.format(data['username']),
                    'accessToken': access_token,
                    'refreshToken': refresh_token
                }, 201
            )
        except:
            return self.response({'message': 'Something went wrong'}, 500)


class UserLogin(BaseResource):
    def post(self):
        data = parser.parse_args()
        current_user = UserModel.find_by_username(data['username'])
        if not current_user:
            return self.response(
                {'message': 'User {} doesn\'t exists'.format(data['username'])}, 401
            )

        if UserModel.verify_hash(data['password'], current_user.password):
            access_token = create_access_token(identity=data['username'])
            refresh_token = create_refresh_token(identity=data['username'])
            return self.response(
                {
                    'message': 'Logged in as {}'.format(current_user.username),
                    'accessToken': access_token,
                    'refreshToken': refresh_token
                }, 300
            )
        else:
            return self.response({'message': 'Wrong credentials'}, 401)


class UserLogoutAccess(BaseResource):
    @jwt_required
    def post(self):
        jti = get_raw_jwt()['jti']
        try:
            revoked_token = RevokedTokenModel(jti=jti)
            revoked_token.add()
            return self.response({'message', 'Access token has been revoked'})
        except:
            return self.response({'message': 'Something went wrong'}, 500)


class UserLogoutRefresh(BaseResource):
    @jwt_refresh_token_required
    def post(self):
        jti = get_raw_jwt()['jti']
        try:
            revoked_token = RevokedTokenModel(jti=jti)
            revoked_token.add()
            return self.response({'message': 'Refresh token has been revoked'})
        except:
            return self.response({'message': 'Something went wrong'}, 500)


class TokenRefresh(BaseResource):
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        access_token = create_access_token(current_user)
        return self.response({'accessToken': access_token})
