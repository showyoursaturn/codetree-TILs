n = int(input())
cnt = 0

while n:
    if n % 2 == 0:
        n = n * 3 + 1
    elif n % 2 == 1:
        n = n * 2 + 2
    cnt += 1
    if n >= 1000:
        break
print(cnt)