n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

def match_number(a,b,c):
    arr = [a,b,c]
    cnt_1, cnt_2 = 0, 0
    for i in range(3):
        if abs(arr[i]-arr1[i]) <= 2 or abs(arr[i]-arr1[i]) >= n-2:
            cnt_1 += 1
        if abs(arr[i]-arr2[i]) <= 2 or abs(arr[i]-arr2[i]) >= n-2:
            cnt_2 += 1
    return cnt_1, cnt_2

result = 0
for a in range(1,n+1):
    for b in range(1,n+1):
        for c in range(1,n+1):
            cnt1, cnt2 = match_number(a,b,c)
            if cnt1==3 or cnt2==3:
                result+=1

print(result)