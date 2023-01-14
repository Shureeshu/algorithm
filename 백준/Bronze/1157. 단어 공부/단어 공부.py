S = input().lower()
A = [0]*(ord('z')-ord('a')+1)

for s in S:
    A[ord(s)-ord('a')] += 1

x = A.index(max(A))
if A.count(max(A)) > 1:
    x = ord('?')-ord('A')

print(chr(x+ord('A')))
