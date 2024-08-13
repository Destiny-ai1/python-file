tp=(1,3,5)
tp1=1,3,5

lst= [1]
print(type(lst))
tp13=1,
print(type(tp13))


#마지막에 원소 추가
my_list=[]
my_list.append(3)
my_list.append(40)
print(my_list)

#원하는 위치에 원소를 추가한다
my_list.insert(1,10)
print(my_list)

#리스트에서 원소를 제거하는법
del my_list[1]
print(my_list)

print(my_list[1])

#리스트의 모든 원소를 지운다
my_list.clear()

#join 메소드         (짜를수있는 다른 변수가 들어있어야된다)
my_list='hello-안녕하세요-도모입니다.'
str_list= my_list.split('-')
print(my_list)

#문자열을 분해해 문자열들의 리스트로
my_list='hello-안녕하세요-도모입니다.'
str_list= my_list.split('-')
print(str_list)

#문자열들의 리스트를 모아서 단일 문자로
my_str2=' '.join(str_list)
print(my_str2)

#리스트와 튜플의 변경
x=['A','B','C']
y='A','B','C'
z='ABC'

x[0]='a'
print(x)
#str은 인덱스로 값을 변경할수 없다.
z[0]='a'