str1 = input()
str2 = input()
str3=""
for i in range(len(str1)):
    if str1[i] == str2[i]:
        str3+='0'
    else:
        str3+="1"

print(str3)