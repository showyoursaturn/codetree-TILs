a,b = map(int, input().split())
c = a // b
if c > 0:
    k = "{0}.".format(c)
else:
    k = "0."

i = 0

while i < 20 :
    s = a%b
    s = (s*10)//b
    k += str(s)
    a = (s*10)%b
    i += 1
print(k)