import flask

app= flask.Flask(__name__)

@app.route('/insa')
def aaa():
    return flask.render_template('/insa.html',name='NYS')

# 8081/list?pageno=10
@app.route('/list')
def bbb():
    # flask.request.args['pageno']               # 만약에 pageno가 없다면 오류가 발생
    pageno=flask.request.args.get('pageno')
    if pageno==None:
        return flask.render_template('list.html',mesege='pageno를 입력하세요')
    return flask.render_template('list.html',mesege=pageno)
    
app.run(debug=True,port=8081)
