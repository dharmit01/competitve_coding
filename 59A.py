s = input()
count_upp = 0
count_low = 0

for i in range(len(s)):
    if s[i].isupper():
        count_upp+=1
    else:
        count_low+=1

if int(count_upp)>int(count_low):
    print(s.upper())
elif int(count_low)>int(count_upp):
    print(s.lower())
else:
    print(s.lower())

    