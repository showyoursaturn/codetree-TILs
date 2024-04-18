cnt = 0
b = 0
while True:
    i = int(input())
    if i > 29:
        break
    cnt += 1
    b += i
print(format(b/cnt, ".2f"))