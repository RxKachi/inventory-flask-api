import os
from flask import Flask
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required

from routes.item import Item, ItemList
from auth_func import authenticate, identity
from routes.user import UserRegister
from utils.constants import DB_URI

# create db tables if not exist
import create_tables

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.environ.get("SECRET_KEY")

api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")
api.add_resource(UserRegister, "/register")

if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(host='0.0.0.0', debug=True, port=8000)
