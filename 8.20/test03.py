import flask

app= flask.Flask(__name__)
#10을 출력하는 플라스크 코드와 html을 작성하시오

@app.route('/square')
def square():
    val=flask.request.args.get('val')
    if val!=None:
        val=int(val)
        return flask.render_template('square.html', val=val)
    return flask.render_template('square.html', mesege='val의 값을입력하세요') 

app.run(debug=True,port=8081)