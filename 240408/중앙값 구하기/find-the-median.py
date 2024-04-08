a,b,c = map(int, input().split())

if a>b:
    if b>=c:
        print(b)
    elif c>=a:
        print(a)
    elif a>c and c>b:
        print(c)
elif b>c:
    if c>=a:
        print(c)
    elif a>=b:
        print(b)
    elif b>a and a>c:
        print(a)
elif c>a:
    if a>=b:
        print(a)
    elif b>=c:
        print(c)
    elif b>c and b>a:
        print(c)