from flask import Flask, request, jsonify, render_template
from flask_pymongo import PyMongo
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# MongoDB connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/tododb"
mongo = PyMongo(app)

@app.route('/todo')
def todo_page():
    return render_template('todo.html')

@app.route('/submittodoitem', methods=['POST'])
def submit_todo():
    data = request.get_json()
    item_name = data.get('itemName')
    item_description = data.get('itemDescription')

    if not item_name or not item_description:
        return jsonify({'message': 'Both fields are required'}), 400

    mongo.db.todos.insert_one({
        'itemName': item_name,
        'itemDescription': item_description
    })

    return jsonify({'message': 'Item stored successfully!'}), 200

if __name__ == '__main__':
    app.run(debug=True)
