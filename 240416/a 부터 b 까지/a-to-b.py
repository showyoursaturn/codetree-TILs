a, b = map(int, input().split())
m = a
for i in range (a, b+1):
    if m > b:
        break
    else:
        print(m, end = " ")
        if m % 2 == 0:
           m += 3
        elif m % 2 == 1:
           m = m * 2