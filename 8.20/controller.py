# controller 는 사용자의 요청을 접수해 응답을 출력하는 기능
# 입력화면 1EA, 출력화면 1EA 

import flask

app= flask.Flask(__name__)


# SSR 방식으로 get한테 요청을 해서 읽기요청or 입력화면을 보여달라고한다
@app.route('/finsh',methods=['GET'])
def start():
    return flask.render_template('finsh.html')

# SSR 방식에서 POST 는 요청을 처리해서 결과를 출력
@app.route('/finsh',methods=['POST'])
def end():
    val= flask.request.form.get('val')
    if val!=None:
        val= int(val)
        result= val*val
        return flask.render_template('finsh2.html', result=result)
    return flask.render_template('finsh2.html',mesege='값을 입력하시오')

app.run(debug=True, port=8081)