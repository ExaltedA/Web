a = int(input())
num = input().split() 
ind = []
i=0
for x in num:
    print(num[i], end = " ")
    i+=2
    if i>=a:
        break
