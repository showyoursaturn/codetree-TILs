cnt = 0
a = 0
b = 0
while True:
    a = int(input())
    if a >= 30:
        break
    cnt += 1
    b += a
print(format((b/cnt), ".2f"))