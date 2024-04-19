a,b,c = map(int,input().split())
call = True

for i in range(a, b+1):
    if i%c==0:
        call=False
        break
if call == False:
    print("NO")
else:
    print("YES")