#2-1 문제

movie= ['닥터스트레인지', '스플릿', '럭키']
print(movie)

movie.append('배트맨')
print(movie)

movie.insert(1,'슈퍼맨')
print(movie)

for i in range(0,len(movie)):
    if movie[i]=='럭키':
        del movie[i]
        break
print(movie)

# movie.remove('럭키')                 #del movie[3]
# print(movie)

movie= ['닥터스트레인지','슈퍼맨', '스플릿', '럭키']
del movie[2::]
print(movie)

abc1=['c','c++','java']
abc2=['python','js','c#']
abcs=abc1+abc2
print(abcs)

num=[1,2,3,4,5,6,7]
max:7
min:1
print('max:',max(num))
