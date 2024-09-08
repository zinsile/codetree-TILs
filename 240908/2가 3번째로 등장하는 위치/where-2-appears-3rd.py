n = int(input())
arr = list(map(int, input().split()))
cnt = 0
for i,a in enumerate(arr):
    if a==2 and cnt==2:
        print(i+1)
        break
    elif a==2:
        cnt+=1