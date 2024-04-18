while True:
    a, b, m = map(str, input().split())
    a = int(a)
    b = int(b)
    print(a*b)
    if m == "C":
        break