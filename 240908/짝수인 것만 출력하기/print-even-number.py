n = int(input())
arr = list(map(int, input().split()))
even = [i for i in arr if i%2==0]
for i in even:
    print(i,end=' ')