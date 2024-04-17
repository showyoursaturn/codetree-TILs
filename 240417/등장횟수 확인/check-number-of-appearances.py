a = []
for i in range(5):
    b = int(input())
    a.append(b)
cnt = 0
for j in a:
    if j % 2 == 0:
        cnt +=1

print(cnt)