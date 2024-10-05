n,m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

B=-1
def re_arr():
    temp = []
    global arr
    for a in arr:
        if a>0:
            temp.append(a)
    arr = temp
    
    

def bomb():
    a = 0
    org_idx = 0
    cnt = 1
    B = 0
    for idx,elem in enumerate(arr):
        if a == elem:
            cnt += 1
        if a != elem:
            if cnt >= m:
                for i in range(org_idx,idx):
                    arr[i] = 0
                B += 1
            a, org_idx = elem, idx
            cnt = 1
        if cnt >= m:
            for i in range(org_idx,idx+1):
                arr[i] = 0
            B += 1
    return B

def simulate():
    global B
    while True:
        if B==0:
            break
        # m개 이상 있는 집합 하나 폭파
        B = bomb()
        re_arr()

        

simulate()

print(len(arr))
for a in arr:
    print(a)