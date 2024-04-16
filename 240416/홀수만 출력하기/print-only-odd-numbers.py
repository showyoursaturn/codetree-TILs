N = int(input())
k = []
ap = []
for i in range (N):
    c = int(input())
    if c % 3 == 0 and c % 2 == 1:
        print(c)