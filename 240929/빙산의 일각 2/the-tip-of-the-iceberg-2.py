n = int(input())
arr = [int(input()) for _ in range(n)]

max_cnt = 0
for i in range(1,max(arr)+1):
    arr = [i-1 for i in arr]
    mountine = False
    cnt = 0
    for a in arr:
        if not mountine and a>0:
            cnt+=1
            mountine = True
        if a<=0:
            mountine = False
    max_cnt = max(max_cnt, cnt)
print(max_cnt)