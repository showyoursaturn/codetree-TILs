c =[]
for i in range(10):
    a = int(input())
    c.append(a)
cnt = 0
for j in c:
    if j % 2 == 1:
        cnt += 1
print(cnt)