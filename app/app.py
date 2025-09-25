from flask import Flask, request, jsonify

app = Flask(__name__)
todos = []

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the DevSecOps To-Do App! Use /todos to manage tasks."})

@app.route('/todos', methods=['GET', 'POST'])
def handle_todos():
    if request.method == 'POST':
        todo = request.json.get('todo')
        if todo:
            todos.append(todo)
            return jsonify({"message": "Todo added"}), 201
        return jsonify({"error": "Invalid input"}), 400
    return jsonify(todos)

if __name__ == '__main__':
    app.run(debug=True)
