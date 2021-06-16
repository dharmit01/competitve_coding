num = int(input())
str1 = list(input())
count=0
for i in range(0,num-1):
    if str1[i] == str1[i+1]:
        count=count+1

print(count)