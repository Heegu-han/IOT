from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<H1>Hello World!</H1>'

@app.route('/user/<name>')
def hello_user(name):
    return '<h1>Hello, ' + name + '</h1>'

if __name__ == "__main__":
    app.run(host="192.168.137.5", port = 5001, debug=True)
