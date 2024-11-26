import random
print('Welcome to Rock, Paper, Scissor Game')
user_wins=0
computer_wins=0
options=['rock','paper','scissor']
while True:
    user_choise=input('Choose Rock, Paper, Scissor or Q to quit').lower()
    if user_choise=='q':
        break
    if user_choise not in options:
        print('Enter the proper choise')
        continue
    options=['rock','paper','scissor']
    rand_no=random.randint(0,2)
    comp_choise=options[rand_no]
    print('Computer picked',comp_choise,'.')
    if user_choise=='rock' and comp_choise=='scissor':
        user_wins+=1
    elif user_choise=='paper' and comp_choise=='rock':
        user_wins+=1
    elif user_choise=='scissor' and comp_choise=='paper':
        user_wins+=1
    elif user_choise==comp_choise:
        continue
    else:
        computer_wins+=1
    print(user_wins,' ',computer_wins)
if user_choise=='q':
    print('See you again')
elif user_wins>computer_wins:
    print('You Wone,Well Done')
else:
    print('You loose')