n = int(input())
line = [0]*202
comm = [list(map(int, input().split())) for _ in range(n)]

for a,b in comm:
    for i in range(a,b+1):
        line[i] += 1
    
print(max(line))