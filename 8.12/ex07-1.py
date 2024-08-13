movie= ['닥터스트레인지','슈퍼맨', '스플릿', '럭키','배트맨']

result=[]
for i in range(0,len(movie)):
    if movie[i]=='스플릿':
        result.append(i)
    elif movie[i]=='배트맨':
        result.append(i)
print(result)   

for i in range(len(result)-1,-1,-1):
    del movie[result[i]]
print(movie)