a,b,c = map(int,input().split())
call = True

for i in range(a, b+1):
    if c%i==0:
        call=False
        break
if call == False:
    print("YES")
else:
    print("NO")