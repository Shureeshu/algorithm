def factorize(n):
    i = 2
    while n > 1 :
        while i <= n:
            if n%i == 0:
                print(i)
                n //= i
            else:
                i += 1

N = int(input())
factorize(N)