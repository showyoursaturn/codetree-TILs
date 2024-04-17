a = []
for i in range (10):
    b = int(input())
    a.append(b)
val = 0
cnt = 0
for j in a:
    if j >= 0 and j <= 200:
        val += j
        cnt += 1
print(val, round((val/cnt),1))