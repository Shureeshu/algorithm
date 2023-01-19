N = 7
n = []
for i in range(N):
    pass
    n.append(int(input()))
n = tuple(n)

odd_n = []
for x in n:
    if x%2:
        odd_n.append(x)
odd_n = tuple(odd_n)

if len(odd_n):
    print(sum(odd_n))
    print(min(odd_n))
else:
    print(-1)