col, temp = map(str,input().split())
temp = int(temp)

alert = []
if temp >= 37:
    if col == "Y":
        alert.append("A")
    else:
        alert.append("B")
elif temp < 37:
    if col == "Y":
        alert.append("C")
    else:
        alert.append("D")
col2, temp2 = map(str,input().split())
temp2 = int(temp2)
if temp2 >= 37:
    if col2 == "Y":
        alert.append("A")
    else:
        alert.append("B")
elif temp2 < 37:
    if col2 == "Y":
        alert.append("C")
    else:
        alert.append("D")
col3, temp3 = map(str,input().split())
temp3 = int(temp3)
if temp3 >= 37:
    if col3 == "Y":
        alert.append("A")
    else:
        alert.append("B")
else:
    if col3 == "Y":
        alert.append("C")
    else:
        alert.append("D")

if alert.count("A")>=2:
    print("E")
else:
    print("N")