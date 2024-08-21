import flask

# backend 프로그램을 생성하자
# backend 프로그램의 역할 : 사용자가 요청을 보낼때까지 대기하다가
# 요청을 받으면 적절한 함수로 실행해준다
# backend 프로그램은 일반적으로 프레임 워크를 사용한다.
# import 해온 플라스크 모듈(폴더) 안에는 다시 클래스와 함수가 적용된다
    #flask.Flask (모듈.클래스.함수)

# web은 80번이 기본 port 인데
# 개발자들은 80번은 쓸수가없다.


app= flask.Flask(__name__)                    #최초 개발자들이 이렇게 정의해둠 (그냥 외워라)

# python만 있는 상태에선 요청을 하더라도 응답해주는게 없으면 실행하더라도 에러가뜬다.
# 응답하기위해선 개발자가 내용을 집어넣어줘야된다.
# 응답할려면 내용은 함수가 return 되어야한다

@app.route('/aaa')                                       
def insa(): 
    print('hello')

# @로 쓰는 용어는 annotation 이라고부른다
# aaa로 요청이 들어오면 insa()를 실행해라


app.run(debug=True,port=8081)                  #최초 개발자들이 이렇게 정의해둠 (그냥 외워라)