import sys

n = int(input())
arr = input().split()
mins = sys.maxsize

for elem in arr:
    elem = int(elem)
    if elem == mins:
        cnt+=1
    elif elem < mins:
        mins = elem
        cnt = 1
print(mins,cnt,end = ' ')