# 변수 선언 및 입력
n = int(input())
arr = [
	int(input())
	for _ in range(n)
]

# 연속하여 동일한 숫자가 나오는 횟수를 구해보며,
# 그 중 최댓값을 갱신합니다.
ans, cnt = 0, 0
for i in range(n):
	# Case 1
	if i >= 1 and arr[i] == arr[i - 1]:
		cnt += 1
	# Case 2
	else:
		cnt = 1
	
	ans = max(ans, cnt)

print(ans)