N = int(input())
members = {}
for i in range(1, N+1):
    name, detail = input().split()
    members[name] = members.get(name, 0) + 1

current = sorted(members.items(), reverse=True)
[print(name[0]) for name in current if name[1]%2]