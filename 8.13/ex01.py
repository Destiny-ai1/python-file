# 2-2 연습문제 list 문제

price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1::])

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[1::2])

nums = [1, 2, 3, 4, 5]
print(nums[::-1])

interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[0],interest[2])

interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(' '.join(interest))

print('/'.join(interest))

interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print('\n'.join(interest))

string = "삼성전자/LG전자/Naver"
print(string.split('[]'))

string = "삼성전자/LG전자/Naver/SK하이닉스/미래에셋대우"
print(' ','[]'.split(interest))

#스퀸스 타입 : 자바나 자바크크립트는 intreble.   str, ;ist ,tuple