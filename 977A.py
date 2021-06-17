a,b=input().split()
a=int(a)

count = 0
if a%10==0:
    print("1")

else:
    for i in range(int(b)):
        if a%10 == 0:
            a=a/10
        else:
            a=a-1
    print(int(a))
