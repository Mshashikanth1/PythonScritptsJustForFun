# this is a  number guss game enjoy;
import random
from colorama import Fore, Back, Style
if 'y'==input(Fore.GREEN+'dou you wanted to play?(y) to play(n) to quit:').lower():
    start,stop=map(int,input('enter the range: ').split())
    com_num=random.randint(start,stop)
    print('HINT:',com_num+1)
    count=0
    while True: 
         guess_num=int(input('enter the guess:'))
         if guess_num != com_num:
             print('wrong')
             count+=1
         else:
             count+=1
             print('got correct at attempt :',count)
             break
print('GoodBye!')
print(Style.RESET_ALL)
