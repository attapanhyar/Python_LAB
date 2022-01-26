Hmarks=0
Lmarks=100
print('Welcome to 21TC Batch')
marks = int(input('Enter the marks for english subject'))
while marks<0 or marks>100:
    print('The number exceeds the limit')
    marks = int(input('Re-enter the marks for english subject'))
 if Hmarks<marks:
    Hmarks=marks
if marks<Lmarks:
    Lmarks=marks
EngM=marks
marks = int(input('Enter the marks for Social Studies subject'))
while marks<0 or marks>100:
    #print('The number exceeds the limit')
    marks = int(input('Re-enter the marks for Social Studies subject'))
if Hmarks<marks:
    Hmarks=marks
if marks<Lmarks:
    Lmarks=marks
ScM=marks
marks = int(input('Enter the marks for Sindhi subject'))
while marks<0 or marks>100:
    #print('The number exceeds the limit')
    marks = int(input('Re-enter the marks for Sindhi subject'))
if Hmarks<marks:
    Hmarks=marks
if marks<Lmarks:
    Lmarks=marks
SiM=marks

avg = (EngM+ScM+SiM)/3
per = (EngM+ScM+SiM)/300*100
if per>=80:
    grade = 'A-1'
elif per>=70:
    grade='A'
elif per>=60:
    grade='B'
elif per>=50:
    grade='C'
else:
    grade = 'F'
print('The average is', avg, ' associated percentage is ',per)
print('The Grade is ',grade)
print('Lowest Marks are: ',Lmarks)
print('Highest Marks are ', Hmarks)