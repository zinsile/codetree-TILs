a,b,c = map(int, input().split())
time1 = 10*24*60 + 11*60 + 11
time2 = (a-1)*24*60 + b*60 + c
print(time2 - time1)