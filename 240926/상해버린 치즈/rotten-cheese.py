n, m, d, s = map(int, input().split())

eating = [list(map(int, input().split())) for _ in range(d)] 
#p,m,t = 몇 번째 사람(p)이 몇 번째 치즈(m)를 언제 먹었는지(t초)

sick = [list(map(int, input().split())) for _ in range(s)]
#p,t = 몇 번째 사람(p)이 언제 확실히 아팠는지(t초)

cheese = [0]*(m+1)

for p,t in sick:
    for p2,m2,t2 in eating:
        if p==p2 and t>t2:
            cheese[m2] += 1

damage_cheese = []
for i,c in enumerate(cheese):
    if c>= len(sick):
        damage_cheese.append(i)

max_people = 0
for d in damage_cheese:
    people = 0
    for p,m,t in eating:
        if d==m:
            people+=1
    max_people = max(max_people, people)

print(max_people)