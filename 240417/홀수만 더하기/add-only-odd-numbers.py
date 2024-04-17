n = int(input())
a = []
for i in range(n):
    a.append(i)
val = 0
for j in a:
    if j % 2 == 1 and j % 3 == 0:
        val += j
print(val)