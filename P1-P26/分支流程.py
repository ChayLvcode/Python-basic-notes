#
# score = int(input('Enter your score: '))
# if score>90:
#     print('Wow, you did it')
#     pass
# elif score>80:
#     print('You did good')
# elif score > 60:
#     print('You pass it')
# else:
#     print('No, you failed')

import random
per = int(input('Choose number [0,1,2]:'))
com = random.randint(0,2)
print('Computer get %d'%com)
if per == com:
    print('Win-win game')
    pass
elif per==0 and com==1:
    print('computer win')
    pass
elif per==1 and com==2:
    print('computer win')
    pass
elif per==2 and com==0:
    print('computer win')
    pass
else:
    print('You win')
    pass