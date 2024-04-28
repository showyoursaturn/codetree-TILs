n = int(input())
for i in range(n):
    for j in range(n):
        if j % 2 == 0:
            print(i+1, end = "")
        elif j % 2 != 0:
            print(4-i, end = "")
    print()