n = int(input())
cnt = 0
for i in range(1, 101):
    if cnt >= n:
        break
    cnt += 1
print(cnt)