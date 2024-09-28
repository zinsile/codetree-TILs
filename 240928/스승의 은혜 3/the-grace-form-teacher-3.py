n,b = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

max_student = 0
for i in range(n):
    arr[i][0] = arr[i][0]/2
    price = 0
    student = 0
    for p,t in sorted(arr):
        if price+p+t>b:
            break
        price += (p+t)
        student += 1
    max_student = max(max_student, student)
    arr[i][0] = arr[i][0]*2

print(max_student)