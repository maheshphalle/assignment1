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
    },
    {
        'id': 3,
        'title': 'Learn Github',
        'description': 'merging all the developers file into remote',
        'done': False
    },
     {
        'id': 4,
        'title': 'Learn Github',
        'description': 'merging all the developers file into remote',
        'done': False
    }
]

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/updateTask', methods=['PUT'])
def updateTask():
    taskInput = request.json
    for task in tasks:
        if task["title"] == taskInput["title"]:
            task["description"] = taskInput["description"]
            break
    else:
        tasks.append(taskInput)
    return jsonify(tasks)

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        abort(404)
    return jsonify({'task': task})

@app.route('/post', methods=["POST"])
def post():
    if request.method == 'POST':
        jsondata = request.get_json(force=True)
        tasks.append(jsondata)
        return ("You are getting a post request")

if __name__ == '__main__':
    app.run(debug=True)
