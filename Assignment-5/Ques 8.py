list=[]
x=int(input("Enter the 1st number:"))
list.append(x)
y=int(input("Enter the 2st number:"))
list.append(y)
z=int(input("Enter the 3st number:"))
list.append(z)
a=int(input("Enter the 4st number:"))
list.append(a)
b=int(input("Enter the 5st number:"))
list.append(b)
c=int(input("Enter the 6st number:"))
list.append(c)
d=int(input("Enter the 7st number:"))
list.append(d)
e=int(input("Enter the 8st number:"))
list.append(e)
f=int(input("Enter the 9st number:"))
list.append(f)
g=int(input("Enter the 10st number:"))
list.append(g)
for i in list:
    if i>0:
        print(i ,"is a positive number")
    if i<0:
        print(i ,"is a negative number")
    if i%2==0:
        print(i ,"is an even number")
    if i%2==1:
        print(i ,"is an odd number")
