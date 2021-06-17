str1 = input()
list1 = list()
for str in str1 :
    if str not in list1:
        list1.append(str)

# print(len(list1))

if len(list1)%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
