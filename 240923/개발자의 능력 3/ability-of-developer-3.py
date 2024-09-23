arr = list(map(int, input().split()))

minpower = 3000000

def diffsum(i,j):
    sum1 = arr[i]+arr[j]
    sum2 = sum(arr) - sum1
    diff = abs(sum1-sum2)
    return diff

for i in range(6):
    for j in range(i+1,6):
        diff = diffsum(i,j)
        minpower = min(minpower, diff)

print(minpower)