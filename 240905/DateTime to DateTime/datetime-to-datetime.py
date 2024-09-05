a,b,c = map(int, input().split())
time1 = 10*24*60 + 11*60 + 11
time2 = (a-1)*24*60 + b*60 + c
result = time2 - time1
if result > 0 :
    print(result)
else : print(-1)