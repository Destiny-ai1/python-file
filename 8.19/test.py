# 숫자 2개를 quertstring를 전달받아 합계를 출력하는 플라스크 코드와 뷰 페이지를 작성하고 실행하시오

import flask

app= flask.Flask(__name__)

@app.route("/add")
def hap():
    num1= int(flask.request.args.get('num1'))
    num2= int(flask.request.args.get('num2'))
    result= num1+num2
    return flask.render_template('add.html',result=result)

app.run(debug=True,port=8081)





# flask를 만들어둔다
# 숫자 2개를 quertstring 전달받을값을 만든다.
# 뷰페이지를 작성하고 실행한다.