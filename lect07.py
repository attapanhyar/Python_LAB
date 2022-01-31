

f = open("demofile.txt", "r")
i = int(1)
for x in f:
    print('Record # {}'.format(i))
    Msg = x.split(',')
    print('The name of the student is: ', Msg[0])
    print('The Roll Number of the student is: ', Msg[1])
    print('Remarks: ', Msg[2])
    print('Grade', Msg[3])
    i = i+1

