from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')

def hello():
    return 'Hello from Flask!!!!'

def home():
    return "Hello, Flask! 🚀"

@app.route('/about')
def about():
    return "This is the About page."

mrashwini_new
@app.route('/api')
def api():
    data = {
        "name": "Ashwini",
        "project": "Flask GitHub Integration",
        "status": "In Progress",
        "features": ["Routing", "Branching", "Merge Conflict Resolution"]
    }
    return jsonify(data)

main

if __name__ == '__main__':
    app.run(debug=True)
