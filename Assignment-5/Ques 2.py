x=int(input("Enter the Lower limit of the range:"))
y=int(input("Enter the Upper limit of the range:"))
z=int(input("Enter the number to check Divisibility with:"))
for i in range(x,y):
    if i%z==0:
     print(i)