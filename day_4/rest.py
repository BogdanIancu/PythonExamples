from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'My first REST API'

@app.route('/get-all', methods=['GET'])
def getAllToDos() :
    return jsonify(['Training Python', \
    'Proiect Facultate'])

@app.route('/add-todo', methods=['POST'])
def addToDo():
    body = request.json
    print(body['todo'])
    return jsonify('Adaugat cu succes')


if __name__ == '__main__':
    app.run(host='localhost', port='9099')