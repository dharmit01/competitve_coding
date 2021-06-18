s= int(input())
s1 = input()
count_A=0
count_D=0
for str in s1:
    if str == 'A':
        count_A+=1
    else:
        count_D+=1

if count_A>count_D:
    print("Anton")
elif count_D>count_A:
    print("Danik")
else:
    print("Friendship")