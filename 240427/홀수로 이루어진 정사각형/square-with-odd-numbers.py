n = int(input())
for i in range(0,2*n,2):
    cnt = 11
    cnt += i
    for j in range(n):
        print(cnt, end = " ")
        cnt += 2
    print()