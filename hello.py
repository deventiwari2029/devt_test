from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello world!'

@app.route('/test')
def test():
    return 'Special Hello world Test!'

@app.route('/mark')
def mark():
    lt = ['harry','ron','hermoine','rupus','neville','dumbul']
    str1 = ""
    for i1 in lt:
        str1 = str1 + "<h1>" + "{}".format(i1) + "</h1><br>"
    st1 = "<html><head></head><body>cast:<br>" + str1 + "</body></html>"
    return st1


