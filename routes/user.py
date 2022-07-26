import sqlite3
from flask_restful import Resource, reqparse

from models.user import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("username", required=True,
                        type=str, help="field is required!")
    parser.add_argument("password", required=True,
                        type=str, help="field is required!")

    @classmethod
    def post(cls):
        data = cls.parser.parse_args()

        user = UserModel.find_by_username(data["username"])
        if user:
            return {"message": "User already exist"}, 400

        user = UserModel(**data)
        try:
            user.save_user()
        except Exception:
            return {"message": "There was an error"}, 500

        return {"message": "user created successfully..."}, 201
