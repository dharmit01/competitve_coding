z=input;i=int;n=[i(z()) for r in ' '*4]
print(sum([any([x%y<1 for y in n]) for x in range(1,i(z())+1)]))
