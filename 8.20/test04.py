#제곱값을 출력하는 플라스크 코드와 html 을 작성하시오
#사용자가 None 인 경우 alert를 이용해 오류 메세지 출력
# 제곱한 값이 100이상인 경우 빨간색, 미만인 경우 파란색
import flask

app=flask.Flask(__name__)

@app.route('/set')
def set():
  val=flask.request.args.get('val')
  if val==None:
    return flask.render_template('set.html', mesege='val을 입력하세요')
  else:
    val=int(val)
    set2= val*val
    return flask.render_template('set.html',val=val, set2=set2)

app.run(debug=True,port=8081)


# get으로 꺼낼땐 args 이고
# post로 가져올땐 form 

# @app.route('/set')
# def set():
#     val=flask.request.args.get('val')
#     if val!=None:
#         return flask.render_template('set.html',val=val)
#     return flask.render_template('set.html',mesege='값을 입력하시오',mesege2='값을 입력하세요')