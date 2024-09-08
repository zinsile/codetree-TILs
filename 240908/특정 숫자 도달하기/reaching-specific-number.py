arr = list(map(int,input().split()))
temp,cnt = 0,0
for i in arr:
    if i > 250:
        break
    else :
        temp += i
        cnt+=1

tempavg = temp/cnt
print(f"{temp} {tempavg:.1f}")