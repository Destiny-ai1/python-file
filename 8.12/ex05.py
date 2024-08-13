#연습문제 1-3

a= "hello"
b= "world"
c= "hello world"
print(a+'!'+b)

print(c*4)

print(a[0:3])

plate= "22가 2210"
print(plate[4:])

string= "홀짝홀짝홀짝"
print(string[::2])

string = "python"
print(string[::-1])

phone ="010-1111-2222"
print(phone[0:3],phone[4:8],phone[9:13])

# 1st = phone.split('-')   변수가 한개 더왔을경우 ('-') 표시인경우 
# phone(1st[0],1st[1],1st[2])

print(phone[0:3]+phone[4:8]+phone[9:13])

string= 'abcd'
print(string.capitalize())                             #capitalize 소문자를 대문자로 바꿔주는형식

string= '국어 영어 수학 과학 경제 물리 지리 생물 화학'
lst= string.split(' ')
for elemet in lst:
    print(elemet) 