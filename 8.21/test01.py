# 숫자 2개를 입력받아 더해서 출력하는 플라스크 웹앱을 만드시오
# /경로를 추가하시오
# /add로 덧셈을 처리하시오
# 오류가 있는 경우 이동후 오류메시지 출력

from flask import Flask , request ,render_template, redirect, flash, get_flashed_messages

app=Flask(__name__)

app.secret_key='1234'

@app.route('/')
def add_in():
    flash_messages =get_flashed_messages()                          #flash된 1회성 메세지를 꺼낸다
    
    messages=''
    if(len(flash_messages)>0):                                      #1회성 메세지가 에러 메세지가 존재할경우
        messages = flash_messages[0]

    return render_template('add_in.html',messages=messages)

# 숫자 2개를 입력받아 보내고 받고 더하기
@app.route('/add', methods=['GET'])
def add():
    return render_template('add.html')

@app.route('/add', methods=['POST'])
def add_out():
    try:
        val=int(request.form.get('val'))
        val2=int(request.form.get('val2'))
        result=val+val2
        return render_template('add_out.html',result=result)
    except(TypeError,ValueError):
        flash('숫자를 입력해주세요')
        return redirect('/')

app.run(debug=True,port=8081)