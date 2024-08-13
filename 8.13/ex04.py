#딕셔너리
#딕셔너리는 자바스크립트의 객체에 해당
#키와 값의 형식으로 데이터를 저장
# JS 객체 : const obj ={name:'summer'}                  딕서녀리에서는  name:키,summer: 값 


my_d= {'irum':'xxx','nai':20}
#키를 지정해서 값을 읽어낸다
a='irum'

#키를 직접 적을수도 있고 변수로 대신할수있다.
print(my_d['irum'])
print(my_d[a])

#키가 없다면 key eroor라고 표시한다
# print(my_d['name'])                          #정해진 키의 값이 없을때

#키와 값의 쌍인 아이템 추가
my_d['email'] = 'we8537@naver.com'
print(my_d)

#삭제하기
del my_d['email']
print(my_d)

#키 뽑아내기
print(list(my_d.keys()))

#값만 추출
print(my_d.values())

#키와 값의 상을 추출
print(my_d.items())
for k in my_d.keys():
    print(k)
#items()를 이용해서 my_d의 각아이템의 키와 값을 출력하시오
for k,name in my_d.items():
    print(k,name)





#boilerplate
# public class xx {
# public static void main (string)
#