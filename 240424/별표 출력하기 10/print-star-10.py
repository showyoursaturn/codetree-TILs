n = int(input())
for i in range(2*n):
    if i%2 == 0:
        for j in range(int(1+(i/2))):
            print("*", end = " ")
    else:
        for j in range(int(n-(i-1)/2)):
            print("*", end = " ")
    print()