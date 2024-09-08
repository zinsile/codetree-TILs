arr = list(map(int, input().split()))
counting = [0]*10
for i in arr:
    if i==0:
        break
    elif i<10:
        continue
    else:
        counting[i//10] +=1

for i,x in enumerate(counting[1:]):
    print(f"{i+1} - {x}")