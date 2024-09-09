# 변수 선언 및 입력
n, m, k = tuple(map(int, input().split()))
penalized_person = [
    int(input())
    for _ in range(m)
]
penalty_num = [0] * (n + 1)

# 각 패널티 횟수를 세서,
# 최초로 K번 이상 벌칙을 받는 사람을 추적합니다.
ans = -1
for target in penalized_person:
    penalty_num[target] += 1

    if penalty_num[target] >= k:
        ans = target
        break

print(ans)