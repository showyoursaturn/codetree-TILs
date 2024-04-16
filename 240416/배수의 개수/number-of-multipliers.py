a = []
for i in range(10):
    b = int(input())
    a.append(b)
cnt = 0
cnt2 = 0
for j in a:
    if j % 3 ==0:
        cnt += 1
    if j % 5 == 0:
        cnt2 += 1
print(cnt, end = " ")
print(cnt2, end = " ")