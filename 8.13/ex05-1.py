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