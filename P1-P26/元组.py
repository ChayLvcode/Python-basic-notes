# # Tuple 无法修改
# # tupleA = () #Empty tuple
# tupleA = ('abcd', 89.12, [1,23,41], 23, 'chay')
# # print(tupleA)
#
# # #元组的查询
# # for item in tupleA:
# #     print(item,end=' ')
#
# #反转，每两个取一次
# print(tupleA[::-2])
# print(tupleA[-4:-2:])


tupleA = (1, 2, 3, 4, [5], 6, 7, 8, 2, 2)
# print(type(tupleA))
# print(tupleA[::-2])
# print(tupleA[-4:-2:])
# print(tupleA[2:4:])

#次数
print(tupleA.count(2))