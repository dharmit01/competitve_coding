rows,cols = map(int, input().split())

#middle of the pattern
middle = rows//2+1

#pattern top part
for i in range(1,middle):
    #calculate number of .|. required
    center = (i*2-1)*".|."
    #print in center and replace other space with -
    print(center.center(cols,"-"))

#print Middle
print("WELCOME".center(cols,"-"))

#print lower part
for i in reversed(range(1,middle)):
    center = (i*2-1)*".|."
    #print in center and replace other space with -
    print(center.center(cols,"-"))