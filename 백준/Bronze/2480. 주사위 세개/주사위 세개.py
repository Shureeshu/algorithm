def prize(x, y, z):
    if x == y:
        if y == z:
            return 10000+1000*x
        else:
            return 1000+100*x
    elif x == z:
        return 1000+100*x
    elif y == z:
            return 1000+100*y
    else:
        return max(x,y,z)*100

x, y, z = list(map(int, input().split()))
print(prize(x, y, z))
