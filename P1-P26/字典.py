dictA = {'Animal':'Cat', 'temp':'20'} #空字典
# print (type(dictA))



dictA['name'] = 'lyf'
dictA['age'] = '32'
dictA['choice'] = 'apple'

print(dictA)

#长度
# print(len(dictA))

#获取key的value
print(dictA['age'])

#可修改
dictA['name'] = 'wlh'
print(dictA)

print(dictA.keys())
print(dictA.values())
print(dictA.items())

for key, value in dictA.items():
    print('%s==%s'%(key,value))

#修改方式
dictA.update({'name':88})
print(dictA)

#删除操作
# del dictA['temp']
# print(dictA)
# dictA.pop('Animal')
# print(dictA)

#字典排序(Key为0， Values为1不过要确认类型一致)
print(sorted(dictA.items(),key=lambda d:d[0]))
