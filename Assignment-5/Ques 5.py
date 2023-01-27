x = 65

for i in range(0,5):
    for j in range(0,i+1):
        char = chr(x)
        print(char,end="")
        x += 1
    print()