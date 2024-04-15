a,b = map(int, input().split())
s = a
k = str(a/b)
i = 0
for i in range (19):
    s = (s*10)%b
    k += str(s)
    i += 1
print(k)