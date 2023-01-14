def d(n):
    return sum([int(x) for x in str(n)])+n
self_numbers = [x+1 for x in range(0, 10000)]

for x in self_numbers:
    if x == 0:
        continue
    else:
        y = d(x)
        while y < 10001:
            self_numbers[y-1] = 0
            y = d(y)
[print(n) for n in self_numbers if n]