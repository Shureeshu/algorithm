import sys

N = int(input())

for n in range(1, N+1):
    sys.stdout.write(' '*(N-n)+'*'*n+'\n')