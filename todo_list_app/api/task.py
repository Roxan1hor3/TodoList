from flask import jsonify, request
from flask_restful import Resource

from todo_list_app import api, db
from todo_list_app.api.error import error_response
from todo_list_app.models import Task


class TaskResource(Resource):
    def get(self, id):
        task = Task.query.get_or_404(id).to_dict()
        data = {'data': task}
        return jsonify(data)

    def put(self, id):
        task = Task.query.get_or_404(id)
        data = request.get_json() or {}
        if data['status'] is True or data['status'] is False:
            task.update_status(data['status'])
        db.session.commit()
        return jsonify(task.to_dict())

    def delete(self, id):
        task = Task.query.get_or_404(id)
        db.session.delete(task)
        db.session.commit()
        return jsonify({'message': f'you delete task {task.id}', 'data': task.to_dict()})


api.add_resource(TaskResource, '/task/<int:id>')


class TasksResource(Resource):
    def get(self):
        filter_dict = {}
        if request.args.get('status'):
            filter_dict['status'] = request.args.get('status')
        if request.args.get('board_id'):
            filter_dict['board_id'] = request.args.get('board_id')
        task_list = Task.query.filter_by(**filter_dict).all()
        data = {'data': [task.to_dict() for task in task_list]}
        return jsonify(data)

    def post(self):
        data = request.get_json() or {}
        if 'body' not in data:
            return error_response(400, 'must include body')
        task = Task()
        task.from_dict(data)
        db.session.add(task)
        db.session.commit()
        return jsonify(task.to_dict())


api.add_resource(TasksResource, '/tasks')
