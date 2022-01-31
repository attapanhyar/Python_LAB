
def intro():    #Function Definition
    print('*********************************')
    print('Welcome to 21TC')
    print('This program shall calculate the Area and Perimeter of a Rectangle')


def area_rect(length,width):    # Function Definition
    return length*width

def perimeter(length,width):
    return 2*length+2*width
intro()     # FUnction call
num1= int(input('Enter the first number'))  # Runtime INput
num2= int(input('Enter the second number')) # Runtime input
perimeter= perimeter(num1,num2)    # Function call
print('The perimeter of rectangle is', perimeter) # Message on the screen
print('The area of the rectangle is :', area_rect(num1,num2))








