a, b = map(int, input().split())
val = 0
if a > b:
    a = b
    b = a
else:
    a = a
    b = b

for i in range (a, b+1):
    if i % 5 == 0:
        val += i
print(val)