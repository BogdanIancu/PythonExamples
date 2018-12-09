from flask import Flask, jsonify, request

app = Flask(__name__)
todos = []

@app.route('/')
def index():
    return 'My first REST WEB API!'

@app.route('/get-all-todos', methods=['GET'])
def get_all_todos():
    return jsonify(todos)

@app.route('/add-todo', methods=['POST'])
def add_todo():
    body = request.json
    todos.append(body)
    return 'Todo Added Successfully'

@app.route('/todo/update', methods=['PUT'])
def update_todo():
    todos[int(request.args.get('id'))]['isDone']=True
    return 'Todo Updated Successfully'

@app.route('/todo/delete/<id>', methods=['DELETE'])
def delete_todo(id):
    todo = todos[int(request.view_args['id'])]
    todos.remove(todo)
    return 'Todo Deleted Successfully'

if __name__ == "__main__":
    app.run(host='localhost', port=9099)