n = int(input())
cnt = 1
cnt1 = n
if n % 2 == 0:
    for i in range(n):
        if i % 2 == 0:
            for j in range(cnt1):
                print("*", end = " ")
            cnt1 -= 1
        else:
            for j in range(cnt):
                print("*", end = " ")
            cnt += 1
        print()
    for i in range(n):
        if i % 2 == 0:
            for j in range(cnt1):
                print("*", end = " ")
            cnt1 -= 1
        else:
            for j in range(cnt):
                print("*", end = " ")
            cnt += 1
        print()