# 반지름을 입력받아 원의 면적을 출력하는 코드를 작성하시오
# radius가 넘어오지 않았다면 alert() 오류 메시지
# 반지름이 100이상이라면 빨간색 아니면 파란색

import flask

app= flask.Flask(__name__)

@app.route('/radius')
def radius():
    radius=flask.request.args.get('radius')
    if radius==None:
        return flask.render_template('radius.html',mesege='값을 입력하세요')
    else:
        radius=float(radius)
        radius2= 3.14*radius*radius 
        return flask.render_template('radius.html',radius=radius, radius2=radius2)


app.run(debug=True,port=8081)