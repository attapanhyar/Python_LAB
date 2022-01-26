

# Welcome to 21TC
eng = eval(input('Enter the marks for English: '))
math = eval(input('Enter the marks for Math: '))
Phy = eval(input('Enter the marks for Phy: '))
obtM = eng+math+Phy
avg = obtM/3
perc = obtM/300*100

if perc>=80:
     print('Congratulation.... You got an A-1 ')
elif perc>=70:
     print('Your grade is A')
elif perc>=60:
     print('Your grade is B')
elif perc>=50:
     print('Your grade is C')
else:
    print('You are fail...')

print('Your average marks are', avg,'and your percentage is ', perc)
