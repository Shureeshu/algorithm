import sys
def merge(A, p, q, r, c):
    i, j, t = p, q+1, 0
    tmp = A[p:r+1]
    while(i <= q and j <=r):
        if A[i]<=A[j]:
            tmp[t] = A[i]
            i += 1
            t += 1
        else:
            tmp[t] = A[j]
            j += 1
            t += 1
    while (i<=q):
        tmp[t] = A[i]
        i += 1
        t += 1
    while (j <= r):
        tmp[t] = A[j]
        j += 1
        t += 1
    i, t = p, 0

    while i <= r:
        A[i] = tmp[t]
        c += 1
        if c == k:

            print(A[i])
            exit()
        i += 1
        t += 1

    return c

def merge_sort(A, p, r, c):
    if p < r:
        q = (p+r)//2
        c = merge_sort(A, p, q, c)

        c = merge_sort(A, q+1, r, c)

        c = merge(A, p, q, r, c)

        return c
    else:
        return c

N, k = map(int, input().split())
A = list(map(int, sys.stdin.readline().split()))
merge_sort(A, 0, N-1, 0)
print(-1)