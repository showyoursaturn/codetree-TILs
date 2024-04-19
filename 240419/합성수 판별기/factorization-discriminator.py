n = int(input())
satis = True
for i in range(2,n):
    if n%i == 0:
        satis = False
        break
if satis == False:
    print("C")
else:
    print("N")