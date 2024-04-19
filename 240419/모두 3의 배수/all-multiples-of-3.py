k = []
s = True
for i in range(5):
    a = int(input())
    k.append(a)
for j in k:
    if j % 3 != 0:
        s = False
        break
if s == False:
    print(0)
else:
    print(1)