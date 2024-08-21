# 사용자 요청에대한 응답하는 프로그램 만들기
    # http서버 에서 돌아가는 프로그램 만들기
    # html > 요청 > 프로그램> 응답 > 사용자 화면에 출력         (flask를 설치)

# 작업중인 파일을 가지고 플라스크 서버를 생성해라
# __name__ 은 플라스크의 내장변수로 현재 작업중인 파일이름
import flask
app=flask.Flask(__name__)

#ex01.html을 만들고
#사용자가 호출할 url 을 지정
@app.route("/")                                     # @란 어노테이션으로 지정
def index():
    return flask.render_template("ex01.html")

#디버그 트루란 코드를 변경하면 서버를 재시작해라 라고 설정
app.run(debug=True,port=8081)
