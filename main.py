import os

operations = '+-*/q'
result = None

def suma(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def dev(a,b): 
    try:
        result = a/b
    except ZeroDivisionError as e:
        os.system('cls')
        print(f'Error: {e}')
        return 
        
    return result


while True:
    operator = input('Choose option(+-*/)\nPress "q" for exit:\n')
    if operator not in operations:
        print('Invalid option!')
        continue
    elif operator == 'q':
        print('See you next time!')
        break
    try:
        num1 = float(input('Enter first: '))
        num2 = float(input('Enter second: '))
    except Exception as e:
        print(f'Error: {e}')
        continue
    if operator == '+':
        result = suma(num1,num2)
    elif operator == '-':
        result = sub(num1,num2)
    elif operator == '*':
        result = mul(num1,num2)
    else:
        result = dev(num1,num2)

    if result != None:
        os.system('cls')
        print(f'Result: {result}')



