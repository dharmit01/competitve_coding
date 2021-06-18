a,b = input().split()
str1 = input().split()
count = 0
for str in str1:
    if int(str)<=int(b):
        count+=1
    if int(str)>int(b):
        count+=2

print(count)

