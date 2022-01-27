def add(x,y):
    sum = x+y
    print('the sum is ',sum) 
def print_profile(roll,name,semester):
    print('Your Roll number is', roll)
    print('Your Name is: ',name)
    print('and your semester is: ', semester)
def listprint(record):
    print('Your Roll number is', record[0])
    print('Your Name is: '  ,record[1])
    print('and your semester is: ', record[2])
    
record = ['21TC54','Abdul Rehman','First']
record1 = ['21TC45','Arsalan','First']
listprint(record)
listprint(record1)

