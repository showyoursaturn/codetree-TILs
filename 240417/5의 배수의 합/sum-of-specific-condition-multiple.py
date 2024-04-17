a, b = map(int, input().split())
val = 0
c = 0
d = 0
if a > b:
    d = a
    c = b
else:
    c = a
    d = b

for i in range (c, d+1):
    if i % 5 == 0:
        val += i
print(val)