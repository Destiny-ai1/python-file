#딕셔너리 2-4 문제

temp={}

ice={'메로나','폴라포','빵빠레'}
money={1000,1200,1800}
zip(ice,money)
for k,v in zip(ice,money):
    print(k,v)

ice2={'죠스바':1200,'월드콘':1500}
for k,v in ice2.items():
    print(k,v)

ice3={'메로나':1000}     
print('메로나 가격:',ice3['메로나'])

ice3['메로나'] = 1300
print(ice3)

del ice3['메로나']
print(ice3)

money={'가격:','메로나:1000','폴라포:1200'}
EA={'재고:',10,3}
print(money,EA)

ice4={'메로나:1000원'+'EA:10','폴라포:1200원'+'EA:3'}
print(ice4)