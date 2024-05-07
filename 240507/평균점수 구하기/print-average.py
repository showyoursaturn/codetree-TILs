s = list(map(float, input().split()))
cnt = 0
for i in s:
    cnt += i
print(round(cnt/len(s),1))