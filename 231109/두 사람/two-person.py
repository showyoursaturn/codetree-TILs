s, g = input().split()
s1, g1 = input().split()

s = int(s)
s1 = int(s1)

if g == 'M' and (s >= 19 or s1 >=19):
    print(1)
elif (g != 'M' or g1 == 'M') and g1 == 'M' and (s>=19 or s1>=19):
    print(1)
else:
    print(0)