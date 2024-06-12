from flask import Flask
from flask_restful import Api
from app.db import init_db
from app.api import UserResource

app = Flask(__name__)
api = Api(app)

init_db(app)

api.add_resource(UserResource, '/users', '/users/<int:user_id>')

if __name__ == '__main__':
    app.run(debug=True)
