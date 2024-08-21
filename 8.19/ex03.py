#  >>의존성관리 방법<<
# 파이썬은 내부, 외부가 많은 라이브러리를 의존하다
# 파이썬 프로젝트가 설치된 모든 라이브러리를 다사용할수있는 상태가아니며 > 필수라 라이브러리만 사용가능
# 필수 라이브러리만 사용하되 필요한 라이브러리는 import 명령으로 가져와라
import flask

# 사용자 요청을 접수해 함수를 호출해줄 서버프로그램이 필요하다
# 서버 프로그램은 flask 모듈의 Falsk 클래스의 객체
# 객체를 생성할때 현재 작업중인 소스 파일이 필요하다
# 파이썬은 __name__ 이라는 시스템 변수를 담아두고있다.

# 함수는 실행하면 처리가 끝나고 종료된다
# 백엔드는 실행하면 사용자가 요청할때마다 실행된다
# 사용자가 요청한 함수가 실행되기 위해 url+함수로 엮는다(binding)
app= flask.Flask(__name__)                   #error 발생하는 제일 쉬운 실수 복붙하고 네임을 안바꿀때

# 이상태로 실행하면 /aaa 에서 함수에 응답하는 코드가 없어서 오류

@app.route('/aaa')
def aaa():
    print('aaa를 실행했어요')

@app.route('/bbb')
def bbb():
    print('bbb를 실행했어요')

app.run(debug=True,port=8081)
