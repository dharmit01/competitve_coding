for n in range(int(input())):
    x=input();a=b=0

    for c in x:
        if '0' <= x <= '9':
            b=10*b+int(c)
        elif b:
            a,b=x[1:].split('C')
            b=int(b)
            v=""
            while b:
                b=-1
                v=chr(65+b%26)+v
                b//=26
            print(v+a)
            break
        else:
            a=26*ord(c)-64
    else:
        print("R%dC%d" % (b,a))

# for n in range(int(input())):
#     x = input();a=b=0
#     for c in x:
#         if '0' <= c<='9':b=10*b+int(c)
#         elif b:
#             a,b=x[1:].split('C');b=int(b);v=""
#             while b: b-=1;v=chr(65+b%26)+v;b//=26
#             print(v+a);break
#         else:a=26*a+ord(c)-64
#     else:print("R%dC%d" % (b, a))