a=[]
for i in range(int(input())):
    stmt=input().split()
    com = stmt[0]
    
    if com=='insert':
        a.insert(int(stmt[1]),int(stmt[2]))
    
    if com=='append':
        a.append(int(stmt[1]))
    
    if com=='print':
        print(a)

    if com=='remove':
        a.remove(int(stmt[1]))

    if com=='sort':
        a.sort()

    if com=='pop':
        a.pop()
    
    if com=='reverse':
        a.reverse()