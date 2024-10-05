n = int(input())
arr = [0]*(n+1)
for i in range(1,n+1):
    arr[i] = int(input())

def block_delete(s,e):
    for i in range(s,e+1):
        arr[i] = 0
    temp = [0]
    for a in arr:
        if a>0:
            temp.append(a)
    return temp

for _ in range(2):
    s, e = map(int, input().split())
    #블럭 빼기
    arr = block_delete(s,e)

print(len(arr)-1)
for t in arr:
    if t != 0:
        print(t)