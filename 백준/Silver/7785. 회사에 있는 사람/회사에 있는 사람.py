N = int(input())
members = {}
for i in range(1, N+1):
    name, detail = input().split()
    members[name] = members.get(name, 0) + 1

current = sorted([name for name in members if members[name]%2], reverse=True)
[print(name) for name in current]