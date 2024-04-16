n = int(input())
kyo = 0
bok = 0
hwa = 0
for i in range(1, n+1):
    if i % 12 == 0:
        hwa += 1
    elif i % 3 == 0:
        bok += 1
    elif i % 2 == 0:
        kyo += 1
    elif i % 2 == 0 and i % 3 ==0:
        bok += 1
    elif i % 2 == 0 and i % 12 == 0:
        hwa += 1
    elif i % 3 == 0 and i % 12 == 0:
        hwa += 1

print(kyo, end = " ")
print(bok, end = " ")
print(hwa, end = " ")