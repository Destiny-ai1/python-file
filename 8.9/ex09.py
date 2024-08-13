# 성적을 입력받아 90점이상 a 80점이상 b  70점이상 c 60점이상 d 아니면 f

# jusum=int(input('점수입력'))
# if jusum>=90:
#     print('A')
# elif jusum>=80:
#     print('B')
# elif jusum>=70:
#     print('C')
# elif jusum>=60:
#     print('D')
# elif jusum>=50:
#     print('f')

#국어와 영어 성적을 입력받아 모두 70점 이상이면 합격,아니면 불합격

ko=int(input('점수입력'))
en=int(input('점수입력'))
if ko>=70 and en>=70:
    print('우수')
elif ko>=70 or en>=70:
    print('합격')
else:
    print('불합격')

#국어와 영어 성적을 입력받아 모두 70점 이상이면 우수, 하나라도 70점이상이면 합격, 아니면 불합격
