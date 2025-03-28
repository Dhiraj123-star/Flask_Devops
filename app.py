from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields

app = Flask(__name__)
api = Api(app, version='1.0', title='Task Management API', description='A simple Task Management API')

# Task Model
task_model = api.model('Task', {
    'id': fields.Integer(readOnly=True, description='The task unique identifier'),
    'title': fields.String(required=True, description='Task title'),
    'description': fields.String(required=False, description='Task description'),
    'status': fields.String(required=True, description='Task status', enum=['pending', 'in-progress', 'completed'])
})

tasks = []  # In-memory storage for tasks
task_counter = 1

@api.route('/tasks')
class TaskList(Resource):
    @api.doc('list_tasks')
    @api.marshal_list_with(task_model)
    def get(self):
        """List all tasks"""
        return tasks

    @api.doc('create_task')
    @api.expect(task_model)
    @api.marshal_with(task_model, code=201)
    def post(self):
        """Create a new task"""
        global task_counter
        task = api.payload
        task['id'] = task_counter
        task_counter += 1
        tasks.append(task)
        return task, 201

@api.route('/tasks/<int:id>')
@api.param('id', 'The task identifier')
@api.response(404, 'Task not found')
class Task(Resource):
    @api.doc('get_task')
    @api.marshal_with(task_model)
    def get(self, id):
        """Get a task by ID"""
        for task in tasks:
            if task['id'] == id:
                return task
        api.abort(404)

    @api.doc('delete_task')
    @api.response(204, 'Task deleted')
    def delete(self, id):
        """Delete a task by ID"""
        global tasks
        tasks = [task for task in tasks if task['id'] != id]
        return '', 204

    @api.doc('update_task')
    @api.expect(task_model)
    @api.marshal_with(task_model)
    def put(self, id):
        """Update a task by ID"""
        for task in tasks:
            if task['id'] == id:
                task.update(api.payload)
                return task
        api.abort(404)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
