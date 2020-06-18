from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/test1")
def test1():
    return "Test!!! Hello World! This is test script"

@app.route("/test2")
def test2():
    return "<html><head></head><body><h1 color='red'>Welcome My first page</h1></body></html>"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=int("5000"), debug=True)