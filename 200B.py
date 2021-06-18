a = int(input())
str1 = input().split()
sum = 0
for str in str1:
    sum += int(str)

print("%.12f" % (sum/a))