a, b = map(int, input().split())
val = 0
c = 0
d = 0
if a > b:
    a = d
    b = c
else:
    a = c
    b = d

for i in range (c, d+1):
    if i % 5 == 0:
        val += i
print(val)