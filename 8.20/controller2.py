#점수를 입력받아 70점이상이면 합격 = 파란색, 아니면 불합격 =빨간색
#점수를 입력 안하면 alert() 
#점수 입력화면 1EA, 출력화면 1EA

from flask import Flask,request,render_template

app= Flask(__name__)

@app.route('/exam07',methods=['GET'])
def jumsu():
    return render_template('exam07_input.html')

@app.route('/exam07',methods=['POST'])
def jumsu2():
    val= request.form.get('val')
    print('=========================')
    print(val=='')
    
    if val!='':
        return render_template('exam07_result.html',val=int(val))
    return render_template('exam07_result.html',mesege='값을 입력하시오')


app.run(debug=True,port=8081)