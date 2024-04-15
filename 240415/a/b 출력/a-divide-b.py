a,b = map(int, input().split())
s = a
k = str(a/b)
for i in range (19):
    s = (s*10)%b
    k += str(s)
print(k)