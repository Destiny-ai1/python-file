import flask

app = flask.Flask(__name__)

# SSR :서버가 html로 응답한다
# CSR :서버가 json 으로 응답+클라리언트 view를 생성

@app.route("/hello",methods=['GET'])
def index():
    return flask.render_template('hello.html')
    #render_template는 SSR 방식으로 응답 => 

@app.route("/hello2")
def hello2():
    pageno =flask.request.args.get('pageno')
    # 위에 표현은 js에서 location.search와 같다.
    # flask.request.args = 딕셔너리 표현

    # flask.request.args['pageno] 방식
    # 지정된 키가없다면 :keyerror

    # flask.request.args.get('pageno') 방식
    # 키가 없을 경우 none 라고 표현
    return flask.render_template('hello2.html',ㅗㅗㅗ=pageno)

app.run(debug=True,port=8081)