from flask import jsonify
from flask_restful import Resource

from todo_list_app import api
from todo_list_app import db
from todo_list_app.models import Board


class BoardsResource(Resource):
    def get(self):
        b = Board()
        db.session.add(b)
        db.session.commit()
        boards_list = Board.query.all()
        data = {'data': [board.to_dict() for board in boards_list]}
        return jsonify(data)


api.add_resource(BoardsResource, '/boards')



