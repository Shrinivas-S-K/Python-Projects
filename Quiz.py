attend=input('Would you like to play a quiz:')
def quiz():
    marks=0
    print('Welcome to the quiz.')
    q1=input('Expand CPU:')
    if q1.lower()=='central processing unit':
        print('correct')
        marks+=1
    else:
        print('hi')
        
    q2=input('Expand GPU:')
    if q2.lower()=='graphics processing unit':
        print('correct')
        marks+=1
    else:
        exit()
    q3=input('Expand MU:')
    if q3.lower()=='memory unit':
        print('correct')
        marks+=1
    else:
        return()
    print('You got',str(marks),'out of 3. Which is ',((marks/3)*100),'%')
if attend.lower()=='yes':
    quiz()
else:
    print('Thank you!')


