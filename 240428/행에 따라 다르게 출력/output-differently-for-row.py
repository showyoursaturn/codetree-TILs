n = int(input())
cnt = 0
cnt1 = 1
for i in range(n):
    for j in range(n):
        if i % 2 == 0:
            cnt += 1
            print(cnt, end = " ")
            cnt1 = cnt
        else:
            cnt1 += 2
            print(cnt1, end = " ")
            cnt = cnt1
    print()