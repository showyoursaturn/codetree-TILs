N = int(input())
cnt = 0
while N :
    N = N // 2
    cnt += 1
    if N // 2 == 0:
        break
print(cnt)