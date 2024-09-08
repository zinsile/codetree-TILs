scores = list(map(int,input().split()))
counting = [0]*11
for s in scores:
    if s == 0:
        break
    elif s<10:
        continue
    else:
        counting[s//10] += 1

t = 100
for i in counting[:0:-1]:
    print(f"{t} - {i}")
    t -= 10