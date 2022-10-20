import random

game = ['rock','paper','scissors']
num = random.randint(0,2)
comp = game[num]

choice = input('Enter choice: rock,paper or scissors: ')
choice = choice.lower()

print('Your choice = ',choice)
print('comp choice = ',comp)

if choice==comp:
  print('Draw')
elif choice=='rock' and comp =='scissors':
  print('You win')
elif choice=='scissors' and comp=='paper':
  print('You win')
elif choice=='paper' and comp=='rock':
  print('You win')
else:
  print('Comp wins')