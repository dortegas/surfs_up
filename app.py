from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello world'

@app.route('/doc')
def second_route():
    return 'This is a second route'