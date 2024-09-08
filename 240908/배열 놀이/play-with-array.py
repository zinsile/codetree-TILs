n,q = map(int, input().split())
arr = list(map(int, input().split()))
for _ in range(q):
    comm = list(map(int, input().split()))
    if comm[0]==1:
        print(arr[comm[1]-1])
        continue
    elif comm[0]==2:
        if comm[1] in arr:
            print(arr.index(comm[1])+1)
        else: print(0)
        continue
    elif comm[0]==3:
        for i in arr[comm[1]-1:comm[2]]:
            print(i,end=' ')
        print()
        continue