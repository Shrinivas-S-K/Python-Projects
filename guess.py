import random
top_range=input('Enter the top range:')
count=0
if top_range.isdigit():
    top_range=int(top_range)
    if top_range <=0:
        print('Enter the number grater then 0 next time!')
        exit()
else:
    print('Enter a digit greater then 0 next time!')
    exit()
rand_no=random.randint(0,top_range)
while True:
    guess=input('Enter your guess:')
    if guess.isdigit():
        guess=int(guess)
    else:
        print('Enter a digit next time!')
        continue
    if guess==rand_no:
        print('Yhe! You guessed it right.')
        count+=1
        break
    else:
        print('You got it wrong')
        count+=1
print('You got the answer in',count,'guesses')
