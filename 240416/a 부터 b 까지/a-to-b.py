a, b = map(int, input().split())
print(a, end = " ")
m = a
for i in range (a, b+1):
    if m % 2 == 0 and m < b:
        m = m + 3
        print(m, end = " ")

    elif m % 2 == 1 and m < b:
        m = m*2
        print(m, end = " ")