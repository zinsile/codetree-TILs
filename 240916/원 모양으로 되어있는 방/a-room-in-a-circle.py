from collections import deque
n = int(input())
people = deque(int(input()) for _ in range(n))
min_dis = 1003*100

for _ in range(n):
    d = 0
    for i in range(n):
        d += people[i]*i
    min_dis = min(min_dis,d)
    num = people.popleft()
    people.append(num)
print(min_dis)