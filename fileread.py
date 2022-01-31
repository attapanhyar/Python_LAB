# READING FROM A FILE
def readfromfile():
    f = open("demofile.txt", "r")
    #print(f.read())
    i = int(1)
    for x in f:
        print('This is record number {}'.format(i))
        record = x.split(',')
        print('The name of student is ', record[0])
        print('The ID of student is ', record[1])
        print('Remarks: ', record[2])
        print('Grade: ', record[3])
        i=i+1
    f.close()
def writeonfile():
    f = open("demofile.txt", "a")
    f.write("Shahnawaz,21tc60, He is playing is PSL,A-")
    f.close()
def addrecord(name,id,remarks,grad):
    f = open("demofile.txt", "a")
    f.write(name+','+id+','+remarks+','+grad)
    f.close
addrecord("Ali","21TC35","He is a nice student","G+")
readfromfile()