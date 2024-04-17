n = int(input())
yun = 0
pyeong = 0
for i in range(1, n+1):
    if i % 100 == 0 and i % 400 != 0:
        pyeong += 1
    elif i % 4 == 0:
        yun += 1

print(yun)