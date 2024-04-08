a,b,c = map(int, input().split())

if a>b:
    if b>=c:
        print(b)
    elif c>=a:
        print(a)
    elif a>c and c>b:
        print(c)
    else:
        print(c)
elif b>c:
    if c>=a:
        print(c)
    elif a>=b:
        print(b)
    elif b>a and a>c:
        print(a)
    else:
        print(a)
elif c>a:
    if a>=b:
        print(a)
    elif b>=c:
        print(c)
    elif b>c and b>a:
        print(c)
    else:
        print(b)
##
elif c>b:
    if b>=a:
        print(b)
    elif a>=c:
        print(a)
    elif a>c and a>b:
        print(c)
    else:
        print(a)
##
elif a>c:
    if c>=b:
        print(c)
    elif b>=a:
        print(a)
    elif b>a and b>c:
        print(a)
    else:
        print(b)
##
elif b>a:
    if a>=c:
        print(a)
    elif c>=b:
        print(b)
    elif c>b and c>a:
        print(b)
    else:
        print(a)