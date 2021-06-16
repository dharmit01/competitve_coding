from math import ceil

m, n, a = [int(i) for i in input().split()]

x=ceil(m/a)
y=ceil(n/a)

print(x*y)