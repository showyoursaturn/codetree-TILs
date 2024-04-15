a,b = map(int, input().split())
m = (a*10)//b
n = (a*10)%b
k = "0."
for i in range(20):
    k += str(m)
    m = (n*10)//b
    n = (n*10)%b
print(k)