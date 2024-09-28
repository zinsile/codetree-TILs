n,b = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

max_student = 0
for i in range(n):
    arr[i][0] = arr[i][0]/2
    tmp = [a+b for a,b in arr]
    price = 0
    student = 0
    for p in sorted(tmp):
        if price+p<=b:
            price += p
            student += 1
    max_student = max(max_student, student)
    arr[i][0] = arr[i][0]*2

print(max_student)