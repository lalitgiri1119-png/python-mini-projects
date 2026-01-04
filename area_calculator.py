print ('========================')
print('    Area Calculator')
print('=========================')

print('1.Triangle')  
print('2.Rectangle') 
print('3.Square') 
print('4.Circle') 
print('5.quit') 

choice = int (input('enter your choiice(1-5):'))
if choice == 1:
    base = float(input('enter base of triangle:'))
    height = float(input('enter height of triangle:'))
    area = 0.5 * base * height
    print('area of triangle is:', area)
elif choice == 2:
    length = float(input('Enter the length of rectangle:'))
    width = float(input('Enter the width of rectangle:'))
    area = length*width
    print('area of Rectangle is:', area)
elif choice == 3:
    side = float (input('Enter  the  side of square:'))
    area  = side*side
    print('area of square is:', area)
elif choice  == 4:
    radius = float (input('enter the radius of circle'))
    area = (3.14*radius*radius)
    print('area of circle is:', area)
else:
    print('You dont choose any option')  
