import math
a,b = int(input()),int(input())
j =0
for x in range(a,b+1):
    j = int(math.sqrt(x))
    if j*j == x:
        print(x)
