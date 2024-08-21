#예외가 발생하면 except로 이동해서 대응한다
def ex01():
    try:
        data= None
        result= int(data)
    except:
        print('숫자 입력')

def ex02():
    try:
        data= ''
        result = int(data)
    except:
        print('숫자입력')

def ex03():
    try:
        pageno=None
        pageno=int(pageno)
    except TypeError:
        print('타입에러')
    except ValueError:
        print('val에러')
ex03()

def ex04():
    try:
        pageno=None
        pageno=int(pageno)
    except(ValueError,TypeError,):                     #벨류 에러와 타입에러 두개는 묶어서 쓸수있다.
        print('입력하세요')
ex04()