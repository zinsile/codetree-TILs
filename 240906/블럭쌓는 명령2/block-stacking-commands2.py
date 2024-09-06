n, k = map(int, input().split())
comm = [list(map(int,input().split())) for _ in range(k)]
block = [0]*101

for a,b in comm:
    for i in range(a,b+1):
        block[i] += 1

print(max(block))