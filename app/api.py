from flask import request
from flask_restful import Resource
from app.models import User
from app.db import db
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

auth = HTTPBasicAuth()

users = {
    "admin": "password"
}

@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None

class UserResource(Resource):
    @auth.login_required
    def post(self):
        json_data = request.get_json(force=True)
        username = json_data.get('username')
        email = json_data.get('email')
        password = json_data.get('password')
        password_hash = generate_password_hash(password)

        new_user = User(username=username, email=email, password_hash=password_hash)
        db.session.add(new_user)
        db.session.commit()
        return {'id': new_user.id}, 201

    @auth.login_required
    def get(self, user_id):
        user = db.session.get(User, user_id)
        if user is None:
            return {'message': 'User not found'}, 404
        return {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'created_at': user.created_at.isoformat()  # Convert datetime to ISO format string
        }

    @auth.login_required
    def put(self, user_id):
        json_data = request.get_json(force=True)
        user = db.session.get(User, user_id)
        if user is None:
            return {'message': 'User not found'}, 404

        user.username = json_data.get('username', user.username)
        user.email = json_data.get('email', user.email)
        if 'password' in json_data:
            user.password_hash = generate_password_hash(json_data['password'])
        db.session.commit()
        return {'message': 'User updated'}, 200

    @auth.login_required
    def delete(self, user_id):
        user = db.session.get(User, user_id)
        if user is None:
            return {'message': 'User not found'}, 404
        db.session.delete(user)
        db.session.commit()
        return {'message': 'User deleted'}, 200
