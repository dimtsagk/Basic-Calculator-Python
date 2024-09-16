num1 = float(input('Give 1st number: '))
op = input('Enter operator (+,-,*,/): ')
num2 = float(input('Give 2nd number: '))

if op == '+':
    print ('The result is: ', num1+num2)
elif op == '-':
    print ('The result is: ', num1-num2)
elif op == '*':
    print ('The result is: ', num1*num2)
elif op == '/':
    print ('The result is: ', num1/num2)
else:
    print ('error')
