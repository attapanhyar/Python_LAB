

marks = eval(input('Enter the marks for subject: '))

while marks<0 or marks > 100:
    print('Invalid Marks....')
    marks = eval(input('Re-Enter the marks for subject: '))
