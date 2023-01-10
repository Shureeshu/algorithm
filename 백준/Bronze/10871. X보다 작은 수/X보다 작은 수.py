import sys

N, X = list(map(int, input().split()))
input = sys.stdin.readline()
A = list(map(int, input.split()))
output = ''
for x in A:
    if x < X:
        output += f'{x} '
sys.stdout.write(output)