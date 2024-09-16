from collections import deque
import sys

n = int(input())
people = deque(int(input()) for _ in range(n))
min_dis = sys.maxsize

for _ in range(n):
    d = 0
    for i in range(n):
        d += people[i]*i
    min_dis = min(min_dis,d)
    num = people.popleft()
    people.append(num)
print(min_dis)