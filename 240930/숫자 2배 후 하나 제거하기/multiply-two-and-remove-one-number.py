import sys
n = int(input())
arr = list(map(int, input().split()))

min_diff = sys.maxsize

def score(removed_idx):
    sub_diff = 0
    prev = -1
    for i in range(n):
        if i==removed_idx:
            continue
        if prev != -1:
            sub_diff += abs(arr[i]-prev)
        prev = arr[i]
    return sub_diff

for i in range(n):
    arr[i] *= 2
    for j in range(n):
        sub_diff = score(j)
        min_diff = min(min_diff,sub_diff)
    arr[i] //= 2

print(min_diff)