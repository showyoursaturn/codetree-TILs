n = int(input())
num = []
for i in range(1, n+1):
    cnt = 0
    for j in range(1, i+1):
        if i % j == 0:
            cnt += 1
    if cnt == 2:
        num.append(i)
for k in num:
    print(k, end = " ")