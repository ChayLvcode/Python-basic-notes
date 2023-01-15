# 地址问题

a = "    hello    "
b = a

#去空格
print(a.strip())
#对比地址
print(id(a))
print(id(b))