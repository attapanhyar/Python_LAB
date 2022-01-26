def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mult(x,y):
    return x*y
def div(x,y):
    return x/y
num = 0
while num == 0:
    num1 = eval(input('Enter the first number'))
    num2 = eval(input('Enter the Second number'))
    MulStr = '''
    Follow the Operations...
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    '''
    print(MulStr)
    chkPnt = int(input('Enter the number for operation'))

    if chkPnt == 1:
        print(add(num1,num2))
    elif chkPnt == 2:
        print(sub(num1,num2))
    elif chkPnt == 3:
        print(mult(num1,num2))
    elif chkPnt == 4:
        print(div(num1,num2))
    num = int(input('Do you want to continue.. if yes press 0'))
print('Exiting.....!')