from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return '<H1>Hello World!</H1>'

@app.route('/user/<name>')
def hello_user(name):
    return f'<h1>Hello, {name} </h1>'

@app.route('/hello')
def hello_name_count():
    name = request.args.get('name')
    count = request.args.get('count')
    result = ""

    for i in range(int(count)):
        result = result + f'<h1>Hello {name}</h1><br>'

    return result


if __name__ == "__main__":
    app.run(host="192.168.137.5", port = 5001, debug=True)
