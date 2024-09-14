arr = list(input())

res = 0
for idx,i in enumerate(arr):
    if i == '(':
        for j in arr[idx+1:]:
            if j == ')':
                res+=1

print(res)