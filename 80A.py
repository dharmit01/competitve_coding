arr=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53]
n,m=map(int, input().split())
if(arr[arr.index(n) + 1] == m):
  print("YES")
else:
  print("NO")