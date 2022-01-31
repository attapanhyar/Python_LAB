
def intro():        # fucntion definition
    print('**************************************')
    print('****** Cirlce Calculator*******')

intro() # function Call

def circle_area(r):     # function Definintion
    area = 3.142*(r*r)  # calculate Area
    return area # return value in main program

def circle_circ(r):     # function definition
    circ = 2*3.142*r    # Calculate Circumpherence
    return circ         # return value in main program

r = int(input('Enter the raduis of the circle'))
area_var = circle_area(r)   # function Call
circ_var = circle_circ(r)   # function Call
print('The Area of the circle is: ', area_var)  # print on Screen
print('THe circumpherence of the cirlce is :', circ_var)    # print on Screen
