# 猜年龄小游戏
# 1. 3次尝试
# 2. 每3次后，询问是否继续，如果Y或y就继续，X或x退出
# 3. 猜对了就退出

import random

age = random.randint(0,100)
times = 0
count = 3


while times <= count:
    if times == count:
        Ask = input('Do you want try again? (Y/N) ')
        if Ask == 'Y' or Ask == 'y':
            times = 0
        elif Ask == 'N' or Ask == 'n':
            print('You loss!')
            break
        else:
            print('Please enter Y/N')
    else:
        Age = int(input('Enter the age you guess: '))
        if Age == age:
            print('You win!')
            break
        elif Age > age:
            print('Guess a smaller one')
            times += 1
        elif Age < age:
            print('Guess a larger one')
            times += 1




