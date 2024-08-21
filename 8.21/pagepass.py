from flask import Flask, redirect,request,render_template,flash,get_flashed_messages

app= Flask(__name__)

app.secret_key='1234'

#페이지1
@app.route('/')
def abc():
    flash_messages =get_flashed_messages()                          #flash된 1회성 메세지를 꺼낸다
    
    messages=''
    if(len(flash_messages)>0):                                      #1회성 메세지가 에러 메세지가 존재할경우
        messages = flash_messages[0]
    
    return render_template('index.html', messages=messages)

#제곱하기 (화면보내기,얻어오기)
@app.route('/square', methods=['GET'])
def square():
    return render_template('square.html')

@app.route('/square', methods=['POST'])
def square2():
    try:
        val= int(request.form.get('val'))
        result= val*val
    # 작업결과를 html로 출력=> 주소유지
        return render_template('square_end.html',result=result)
    except(TypeError,ValueError):
        flash('숫자를 입력해주세요')
        return redirect('/')
    #새로운 작업

app.run(debug=True,port=8081)