from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def hello():
    return 'Hello from Flask!!!!'

def home():
    return "Hello, Flask! 🚀"

@app.route('/about')
def about():
    return "This is the About page."


if __name__ == '__main__':
    app.run(debug=True)
