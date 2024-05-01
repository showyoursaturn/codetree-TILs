n = int(input())
cnt = 65
for i in range(n):
    for j in range(0, i):
        print(" ", end = " ")
    for j in range(n-i):
        print(chr(cnt), end = " ")
        cnt += 1
    print()