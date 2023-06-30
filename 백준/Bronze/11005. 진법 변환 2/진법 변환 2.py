# 입력
N, B = map(int, input().split())

# 변환
b = int(B)
answer = ''
toB = {}
for x in range(0, 10):
    toB[x] = str(x)
for x in range(10, 36):
    toB[x] = chr(x + 55)

while N > 0:
    N, digit = divmod(N, B)
    answer += toB[digit]
    
# 출력
print(answer[::-1])