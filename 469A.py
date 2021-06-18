n = int(input())
print(['Oh, my keyboard!', 'I become the guy.'][len(set(input().split()[1:]+input().split()[1:])) == n])