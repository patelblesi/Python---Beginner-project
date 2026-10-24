import random
'''
1 for snake
-1 for water
0 for gun
'''

computer = random.choice([-1,0,1])
userstr = input('enter your choice : ')
youDict = {'s':1 , 'w' : -1 , 'g' : 0 }
reverseDict = {1:'s' ,-1: 'w' ,0: 'g'}


you = youDict[userstr]

print(f'you chose{reverseDict[you]}\nComputer chose {reverseDict[computer]}')

if you == computer:
    print("Tie!")
elif (you == 1 and computer == -1) or \
     (you == -1 and computer == 0) or \
     (you == 0 and computer == 1):
    print("You win!")
else:
    print("You lose!")