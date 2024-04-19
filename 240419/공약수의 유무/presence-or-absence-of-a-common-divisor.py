a,b = map(int, input().split())
sat = True
for i in range(a,b+1):
    if 1920%i == 0 and 2880%i == 0:
        sat = False
        break
if sat = False:
    print(1)
else:
    print(0)