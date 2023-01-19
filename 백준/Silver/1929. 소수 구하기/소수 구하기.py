def isPrime(n):
    if n == 1:
        return 0
    if n < 10:
        if n in [2, 3, 5, 7]:
            return 1
        else:
            return 0
    if n < 100:
        for x in [2, 3, 5, 7]:
            if n%x == 0:
                return 0
        return 1
    # 100 < n < 1000
    if n < 1000:
        for x in prime_numbers_1000:
            if x > 31:
                return 1
            if n%x == 0:
                return 0
        return 1
    # 1000 < n
    for x in prime_numbers_1000:
        if x > n**(1/2):
            return 1
        if n%x == 0:
            return 0
    return 1

M, N = map(int, input().split())

prime_numbers_1000 = [2, 3, 5, 7]

for i in range(11, 1000):
    if isPrime(i):
        prime_numbers_1000.append(i)

for x in range(M, N+1):
    if isPrime(x):
         print(x)