a,b = map(int, input().split())
m = ""
if a > b:
    m = "{0}.".format(a//b)
else:
    m = "0."

i = 0
while i < 20 :
    k = a%b
    k = (k*10)//b
    m += str(k)
    a = (k*10)%b
    i += 1
print(m)