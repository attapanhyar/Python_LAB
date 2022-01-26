#A function is a block of code which only runs when it is called.
#You can pass data, known as parameters, into a function.
#A function can return data as a result.

def my_function():      #function Definition
  print("Hello from a function")
#my_function() # function Call


def add(x,y):
    return x+y

#If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
#This way the function will receive a tuple of arguments, and can access the items accordingly:

def add(*args):
    for i in range(len(args)):
        sum = args[i]
    print('The total sum is ', sum)


def my_function(**kwargs):
    print('His last name is ', kwargs["address"])
#my_function(fname="Ali", lname="Labuschagne", cast ='Soomro', address='Shahbeedbenazirabad')


## function with a default value
def address(city='Hyderbad'):
    print('He lives in ', city)

address('Jam shoro')
address('Karachi')
address()
address('Moro')
def isPrime(number):
    flag =True
    for i in range(2,number):
        if number%i==0:
            flag = False
    return flag
