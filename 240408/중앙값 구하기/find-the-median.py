a,b,c = map(int, input().split())

if a>b:
    if b>c:
        print(b)
    elif c>b and a>=c:
        print(c)
    else:
        print(a)
elif b>a:
    if c>b:
        print(b)
    elif c>a and c>=b:
        print(c)
    else:
        print(a)