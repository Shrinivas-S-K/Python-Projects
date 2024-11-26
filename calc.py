6print('Enter the two operands:')
op1=int(input('operand1:'))
op2=int(input('operand2:'))
print('Enter the operation you want to perform(+,-,*,/):')
op=(input())
if (op=='+'):
    print(op1+op2)
elif(op=='-'):
    print(op1-op2)
elif(op=='*'):
    print(op1*op2)
else:
    print(op1/op2)