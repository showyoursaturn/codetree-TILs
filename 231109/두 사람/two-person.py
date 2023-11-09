s, g = input().split()
s1, g1 = input().split()

s = int(s)
s1 = int(s1)

if (s >= 19 or s1 >= 19) and (g == 'M' or g1 == 'M'):
    print(1)
else:
    print(0)