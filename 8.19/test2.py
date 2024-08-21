#첫번째  두번째에 input 쓰되 서버로 넘기면 서버에서 select 값이 +면 더해서, -면 빼서 출력하시오

import flask

app= flask.Flask(__name__)

@app.route("/add")
def hap():
    num1= int(flask.request.args.get('num1'))
    num2= int(flask.request.args.get('num2'))
    op= flask.request.args.get('op')
    if op=='-':
        result= num1-num2
    else :
        result= num1+num2
    return flask.render_template('add.html',result=result)

    
app.run(debug=True,port=8081)