for n in range(int(input())):
    s=input()
    length = len(s)
    w=""

    if(length>10):
        w+=s[0]
        w+=str(length-2)
        w+=s[-1]
        print(w)
    
    else:
        w+=s
        print(w)