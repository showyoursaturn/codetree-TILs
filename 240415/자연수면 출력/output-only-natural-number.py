a, b = map(int, input().split())
if type(a) == int and a>0:
    for i in range(b):
        print(a, end="")
elif type(a) == int and a<=0:
    print("0")