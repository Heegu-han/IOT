from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    html = "<html><head></head><body>"
    html = html + "<h1>Hello,heegus!</h1>"
    html = html + "</body></html>"
    return html

@app.route("/test")
def test():
    return "Test"

if __name__ == "__main__":
    app.run(host="192.168.137.5",port=5001,debug=True)
