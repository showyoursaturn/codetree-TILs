N = int(input())
a = input()
a = a.split()

def two(a):
    for j in a:
        if int(j)%2 == 0:
            print(int(int(j)/2), end = " ")
        else:
            print(int(j), end = " ")
two(a)