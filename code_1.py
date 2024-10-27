from flask import Flask, jsonify, request, abort

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': 'Buy groceries',
        'description': 'Milk, Cheese, Pizza, Fruit',
        'done': False
    },
    {
        'id': 2,
        'title': 'Learn Python',
        'description': 'Need to find a good Python tutorial on the web',
        'done': False
    }
]


@app.route ('/task', method=['GET'])

def get_tasks()
    return jsonify({'tasks':tasks})


@app.route ('/task/<int:task_id>',method=['GET'])
def get_task(task.id):
        task = next((task for task in tasks['id'] == task_id)), None)

        if task is none:
                abort(404)

        return jsonify({'task':task})