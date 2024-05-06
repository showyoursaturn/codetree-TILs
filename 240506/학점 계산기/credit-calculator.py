n = int(input())
cnt = 0
m = list(map(float,input().split()))
for i in m:
    cnt += i
a = round(cnt/n , 1)
print(a)
if a >= 4.0:
    print('Perfect')
elif a >= 3.0 and a < 4.0:
    print('Good')
else:
    print('Poor')