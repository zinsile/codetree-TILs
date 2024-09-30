n = int(input())
commd = [list(map(int, input().split())) for _ in range(n)]

score = [0]*4
for i in range(1,4):
    tmp = [0]*4
    tmp[i] = 1
    for a,b,c in commd:
        tmp[a],tmp[b] = tmp[b],tmp[a]
        if tmp[c] == 1:
            score[i] += 1
print(score.index(max(score)))