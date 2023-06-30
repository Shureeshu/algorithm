# 입력
N, B = input().split()
n = 0
b = int(B)
i = 1
for _ in N[::-1]:
    if _ in '0123456789':
        j = int(_)
    else:
        j = int(ord(_)-ord('A'))+10
    n += j*i
    i *= b

# 출력
print(n)