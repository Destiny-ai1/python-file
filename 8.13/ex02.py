# a= (3,4)
# b= 3,4

# #원소 1개를 만든다
# c=3,

# #tuple 를 이용해 한번에 여러개의 변수를 생성
# a,b = 3,4

#js에서 irum과 nai 를가진 객체 ob가 있다 객체의 속성을 풀어 해쳐 대입한다
# const irum= ob.irum
# const nai = ob.nai 

x,y= 10,20
# x,y=y,x
# print(x,y)

z=y
y=x
x=z
print(x,y)

#배열을 tuple로 나타내는 방법
my_list =[1,3,5,7]
my_tuple =tuple(my_list)
print(my_tuple)

#중복된 값을 없앨때 쓰는방법
my_list =[1,3,5,7,7,10]
my_set=set(my_list)
my_list3=list(my_set)
print(my_list3)