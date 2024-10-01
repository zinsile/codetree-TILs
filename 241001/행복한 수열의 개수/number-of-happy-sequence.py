n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
seq = [0]*n

def is_happy_sequence():
    cnt, max_cnt = 1, 1
    for i in range(1,n):
        if seq[i-1] == seq[i]:
            cnt += 1
        else:
            cnt = 1
        
        max_cnt = max(max_cnt, cnt)
    
    return max_cnt >= m

num_happy = 0

#가로
for i in range(n):
    seq = graph[i][:]

    if is_happy_sequence():     ## if is_happy_sequence  vs  if is_happy_sequence()는 결과가 달라짐!
        num_happy += 1

#세로
for i in range(n):
    for j in range(n):
        seq[j] = graph[j][i]
    if is_happy_sequence():
        num_happy += 1

print(num_happy)