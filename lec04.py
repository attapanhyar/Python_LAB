# num = 105
# if num%2 == 0:
#     print('Its a even number')
# else:
#     print('ODD')

eng = int(input('Enter the marks for ENglish'))
comp = int(input('Enter the marks for Computer'))
app_p = int(input('Enter the marks for Applied Physics'))
obt_m = eng+comp+app_p
perc = obt_m/300*100
print('The accumulated percentage is: ', perc)

if perc>=50:
    print('Congratulations! you are pass')
else:
    print('Shabas thai putr')