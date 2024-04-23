n = int(input())
for i in range(n):
    for j in range(n+i, 2*n):
        print("*", end = "")
    for j in range(n, n+i):
        print(" ", end = "")
    for j in range(n, n+i):
        print(" ", end = "")
    for j in range(n+i, 2*n):
        print("*", end = "")
    
    print()