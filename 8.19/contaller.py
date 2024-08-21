import flask

app= flask.Flask(__name__)

@app.route("/add")
def hap():
    num1= int(flask.request.args.get('num1'))
    num2= int(flask.request.args.get('num2'))
    result= num1+num2
    # result2= num1-num2
    return flask.render_template('add.html',result=result)

app.run(debug=True,port=8081)