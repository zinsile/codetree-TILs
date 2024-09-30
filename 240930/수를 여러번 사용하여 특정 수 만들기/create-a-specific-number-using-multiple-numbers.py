a,b,c = map(int, input().split())

max_score = 0
for i in range(0,c//a+1):
    for j in range(0,c//b+1):
        score = (i*a) + (j*b)
        if score <= c:
            max_score = max(max_score, score)
print(max_score)