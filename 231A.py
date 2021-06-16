count=0
for n in range(int(input())):
    a,b,c=input().split()

    if a==b=='1' or b==c=='1' or a==c=='1' or a==b==c=='1' :
        count = count + 1
    
print(count)