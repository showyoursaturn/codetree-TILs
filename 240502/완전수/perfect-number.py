start, end = map(int, input().split())
cnt1 = 0
for i in range(start, end+1):
    cnt = 0
    for j in range(1, i):
        if i % j == 0:
            cnt += j
    if i == cnt:
        cnt1 += 1

print(cnt1)