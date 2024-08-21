import flask

app = flask.Flask(__name__)

@app.route('/')
def x():
    return flask.render_template("ex03.html")

@app.route('/insa2')
def y():
    return flask.render_template("insa2.html")

app.run(debug=True,port=8081)