S = input().lower()
A = [0]*(ord('z')-ord('a')+1)

for s in S:
    A[ord(s)-ord('a')] += 1

x = A.index(max(A))
for n in A[x+1:]:
    if n == max(A):
        x = ord('?')-ord('A')
        break

print(chr(x+ord('A')))