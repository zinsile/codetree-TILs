n = int(input())
arr = [int(input()) for _ in range(n)]

def carry(x,y,z):
    xl,yl,zl = list(str(x)), list(str(y)), list(str(z))
    sumlist = [0]*max(len(xl),len(yl),len(zl))
    for idx,i in enumerate(xl[::-1]):
        sumlist[idx] += int(i)
    for idx,i in enumerate(yl[::-1]):
        sumlist[idx] += int(i)
    for idx,i in enumerate(zl[::-1]):
        sumlist[idx] += int(i)
    temp = False
    for s in sumlist:
        if s>10:
            temp = True
    if not temp:
        return (x+y+z)
    else: return (0)
    
maxres = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            m = carry(arr[i],arr[j],arr[k])
            maxres = max(maxres,m)

print(maxres)