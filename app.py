from flask import Flask, request, jsonify, render_template
from flask_pymongo import PyMongo
from flask_cors import CORS
 HEAD

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


 HEAD

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


import uuid
import hashlib

app = Flask(__name__)
CORS(app)

# MongoDB connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/tododb"
mongo = PyMongo(app)

# HTML To-Do Form (GET/POST with ID, UUID, Hash)
@app.route('/todo', methods=['GET', 'POST'])
def todo():
    item_id = None
    item_uuid = None
    item_hash = None
    if request.method == 'POST':
        item_id = request.form.get('item_id')
        if item_id:
            item_uuid = str(uuid.uuid4())
            item_hash = hashlib.sha256(item_id.encode()).hexdigest()
    return render_template('todo.html', item_id=item_id, item_uuid=item_uuid, item_hash=item_hash)

# API-based To-Do Submission (JSON input)
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

@app.route('/')
def hello():
    return 'Hello from Flask!!!!'

@app.route('/about')
def about():
    return "This is the About page."

@app.route('/api')
def api():
    data = {
        "name": "Ashwini",
        "message": "This is sample API response"
    }
    return jsonify(data)

 6053934 (Add Item ID field only)
 90d4a10 (Restore project structure and continue after rebase)
if __name__ == '__main__':
    app.run(debug=True)

