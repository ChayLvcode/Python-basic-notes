# 九九乘法表
# row = 1
# while row <= 9:
#     col = 1
#     while col <= row:
#         print('%d*%d=%d'%(row,col,row*col),end = ' ')
#         col+=1
#         pass
#     print()
#     row+=1
#     pass

# row = 9
# while row >= 1:
#     col = 1
#     while col <= row:
#         print('%d*%d=%d'%(row,col,row*col),end = ' ')
#         col+=1
#         pass
#     print()
#     row-=1
#     pass

#打印直角三角形
# row = 1
# while row<=7:
#     j=1
#     while j<=row:
#         print('*',end=' ')
#         j+=1
#         pass
#     print()
#     row+=1

# row = 10
# while row >= 1:
#     j = 1
#     while j<=row:
#         print('*',end=' ')
#         j+=1
#         pass
#     print()
#     row -= 1

# for data in range(50,200):
#     if data%2==0:
#         print('%d is even' %data)
#         pass

# for item in 'I love Python':
#     if item == 'P':
#         continue
#     print(item, end=' ')

acc = 'zcy'
pwd = '123'

for i in range(3):
    zh = input('Input account: ')
    pw = input('Enter Password: ')
    if zh == acc and pw == pwd:
        print('Succesfully logged in')
        break
    elif zh != acc:
        print('Wrong account')
    elif pw != pwd:
        print('Wrong Password')
    pass
else:
    print('Account has benn locked')
