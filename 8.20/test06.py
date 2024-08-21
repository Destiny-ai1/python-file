from flask import Flask,request,render_template
from math import pi

app= Flask(__name__)

@app.route('/radius')
def radius():
    radius= request.args.get('radius')
    if radius!=None:
        radius= float(radius)
        radius2= pi*radius*radius
        return render_template('radius.html',radius=radius, radius2=radius2)
    return render_template('radius.html',mesege='값을 입력하시오')

app.run(debug=True,port=8081)