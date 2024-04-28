n = int(input())
cnt = 1
cnt1 = 1
for i in range(n):
    for j in range(n):
        if i % 2 == 0:
            print(cnt, end = " ")
            cnt += 1
            cnt1 = cnt + n - 1
        else:
            print(cnt1, end = " ")
            cnt1 -= 1
            cnt = cnt1 + n + 1
    print()