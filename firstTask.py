HMarks=0
LMarks=100
marks = int(input('Input Marks for English'))
while marks<0 or marks>100:
    print('Invalid Marks.. Marks should between  \(0,100\)')
    marks = int(input('Input Marks for English'))
EngM = marks
if HMarks<EngM:
    HMarks=EngM
if LMarks>EngM:
    LMarks=EngM
marks = int(input('Input Marks for Maths'))
while marks<0 or marks>100:
    print('Invalid Marks.. Marks should between  \(0,100\)')
    marks = int(input('Input Marks for Maths'))
MathM = marks
if HMarks<MathM:
    HMarks=MathM
if LMarks>MathM:
    LMarks=MathM
marks = int(input('Input Marks for Science'))
while marks<0 or marks>100:
    print('Invalid Marks.. Marks should between  \(0,100\)')
    marks = int(input('Input Marks for Science'))
SciM = marks
if HMarks<SciM:
    HMarks=SciM
if LMarks>SciM:
    LMarks=SciM
obtM = EngM+MathM+SciM
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
print('The Highest Marks are', HMarks)
print('The lowest Marks are', LMarks)