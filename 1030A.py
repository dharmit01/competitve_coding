a = int(input())
str1 = input().split()
count = 0
for str in str1:
    if str == '1':
        count+=1

if count!=0:
    print("HARD")
else:
    print("EASY")