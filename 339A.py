str1 = input().split("+")
str2 = ""
str1.sort()

for str in str1:
    str2+=(str+"+")

print(str2[:-1])