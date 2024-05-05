n = list(map(int, input().split()))
cnt = 0
num = 0
for i in n:
    if i <= 250:
        cnt += i
        num += 1
    else:
        break
print(cnt, round(cnt/num, 1))