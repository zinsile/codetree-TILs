counting = [0]*10
n = int(input())
arr = list(map(int, input().split()))
for i in arr:
    counting[i] += 1
for i in counting[1:]:
    print(i)