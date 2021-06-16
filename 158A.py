n,m = input().split()
m = int(m)
a=input().split(" ")
count=0
b=int(a[m-1])
for i in range(int(n)):
    if(int(a[i])>0):
        if int(a[i]) >= b:
            count=count+1

print(count)