s, g = input().split()
s1, g1 = input().split()

s = int(s)
s1 = int(s1)

if g == 'M' or g1 == 'M':
    if s >= 19 or s1 <= 19:
        print(1)
    else:
        print(0)