n = int(input())
for i in range(n):
    for j in range(1, i+1):
        print(" ", end = " ")
    for j in range(n-i, 0, -1):
        print(j, end = " ")
    print()