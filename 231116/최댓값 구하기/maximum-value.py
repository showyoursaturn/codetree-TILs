a,b,c = map(int,input().split())
if a>b:
    if b>=c:
        print(a)
    elif c>a:
        print(c)
    elif c==a:
        print(a)
elif b>c:
    if c>=a:
        print(b)
    elif a>b:
        print(a)
    elif a==b:
        print(b)
elif c>a:
    if a>=b:
        print(c)
    elif b>c:
        print(b)
    elif b==c:
        print(b)
elif b>a:
    if a>=c:
        print(b)
    elif c>b:
        print(c)
    elif c==b:
        print(b)
elif a>c:
    if c>=b:
        print(a)
    elif b>a:
        print(b)
    elif a==b:
        print(a)
elif c>b:
    if b>=a:
        print(c)
    elif a>c:
        print(a)
    elif c==a:
        print(c)