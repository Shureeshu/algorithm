S = set()
i = 1
x = int(input())
S.add(x%42)
while i < 10:
    i += 1
    x = int(input())
    S.add(x%42)

print(len(S))