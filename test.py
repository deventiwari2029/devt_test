from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/test1")
def test():
    return "Test!!! Hello World! This is test script"

@app.route("/test2")
def test():
    return "<html><head></head><body><h1>Welcome My first page</h1></body></html>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)