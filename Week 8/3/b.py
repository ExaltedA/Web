a,b,c,d = int(input()),int(input()),int(input()),int(input())
for x in range(a,b+1):
    if x%d == c:
        print(x, end =" ")