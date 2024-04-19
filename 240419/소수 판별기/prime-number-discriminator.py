n = int(input())
t = True
for i in range(2,n):
    if n%i==0:
        t = False
        break
if t == False:
    print("C")
else:
    print("P")