n = int(input())
arr = [1,n]
index = 2
print(arr[0],arr[1],end=' ')
while True:
    new = arr[index-1]+arr[index-2]
    print(new,end=' ')
    arr.append(new)
    index+=1
    if new>100:
        break