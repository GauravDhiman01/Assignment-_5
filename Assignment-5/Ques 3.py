x=int(input("Enter the 1st side of the triangle:"))
y=int(input("Enter the 2st side of the triangle:"))
z=int(input("Enter the 3st side of the triangle:"))
s=(x+y+z)/2
Area=(s*(s-x)*(s-y)*(s-z))**0.5
if (x+y>z and y+z>x and z+x>y):
    print("Area of the Triangle is " ,Area)
else:
    print("The Triangle dose not exist")