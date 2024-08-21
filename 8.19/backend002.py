import flask

app = flask.Flask(__name__)

@app.route('/')
def bbb():
    return flask.render_template("ex02.html")

@app.route('/insa')
def aaa():
    return flask.render_template("insa.html")

app.run(debug=True,port=8081)