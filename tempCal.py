#1. Expressions
#2. Variables
#3. Assignment

#celsui = int(input("Enter the value in Celcuis"))
#far = 9/5*celsui+32
#print("The equivalent value in Farenhiet is :", end="")
#print(far)

#x,y = eval(input("Enter two numbers separted by comma"))  #Simultaneous Assignemt
#sum,dif = x+y, x-y
#print(sum,dif)

#Things to Ponder...
#print(3,7)
#print(3,4,3+4)
#print()
#print("3+4= ",3+4)

# Following program does swapping
# x = 4
# y = 3
# x,y=y,x
# print(x,y)

#avg.py
# num1 = int(input('Enter the first Integer '))
# num2 = int(input('Enter the second integer '))
# averg = (num1+num2)/2
# print('The average of both numbers is ',averg)

#rectangle.py
#write a program that prompts user to input length and width of a rectangle
#and and print the total area of that rectangle
# print('This program calculates the Area of Triangle <Meters> ')
# lrect = int(input('Input the length of triangle <Meters>'))
# wrect = int(input('Input the width of triangle'))
# Arect = lrect*wrect
# print('The total area of the rectangle is ', Arect, ' in meter sq')

#dis.py
#distance b/w two points
#x1,y1 = eval(input('Enter the first point'))
#x2,y2 = eval(input('Enter the second point'))
#dist = ((x2-x1)**2+(y2-y1)**2)**(0.5)
#print('The distance between P1(',x1,',',y1,')and P2(',x2,',',y2,') is: ', dist)


##quardratic.py
# import math
# print('This program calculates the real roots of quadratic equation')
# a = float(input('Enter the coefficient "a"'))
# b = float(input('Enter the coefficient "b"'))
# c = float(input('Enter the coefficient "c"'))
# discRoot = math.sqrt(b**2-4*a*c)
# root1 = (-1*b+discRoot)/(2*a)
# root2 = (-1*b-discRoot)/(2*a)
# print('The solutions are :',root1,',',root2)




#Branching
#if else
#if elif

num1 =int(input('Input the number'))
if num1%2==0:
    print('The number is Even')
else:
    print('The number is odd')




#future.avg
# print('This program calculates the future value')
# print('of 10 years inverstment')
# principal = int(input('Enter the principal amount'))
# apr = float(input('Enter the annual percentage rate'))
# for i in range(10):
#     principal = principal*(1+apr)
# print('The value after 10 years shall be ', principal)


