snack={'산도':3000,'초코파이':2000,'양갱':1500}
new_snack={'새우깡':1500}
snack.update(new_snack)
print(snack)

str='hello'
str1= str.capitalize()
print(str)
print(str1)

keys=['아맛나','폴라포','탱크보이']
vals=[500,700,1000]
zip(keys,vals)
for key,val in zip(keys,vals):
    print(key,val)