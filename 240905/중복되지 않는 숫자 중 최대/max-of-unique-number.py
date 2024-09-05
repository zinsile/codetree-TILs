n = int(input())
nums = list(map(int, input().split()))

maxn = -1

for num in nums:
    count = 0
    if num > maxn:
        for num2 in nums:
            if num2 == num:
                count+=1
        if count == 1:
            maxs = num

print(maxs)