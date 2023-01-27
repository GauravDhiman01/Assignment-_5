def reverse(str):
    temp=' '
    for i in str:
        temp=i+temp
    return temp
x=str(input('Enter the string you want to be reversed:'))
print(reverse(x))
