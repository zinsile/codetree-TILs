n,b = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

max_student = 0
for i in range(n):
    tmp = [arr[j] for j in range(n)]
    tmp[i][0] = tmp[i][0]/2
    tmp = [a+b for a,b, in tmp]
    price = 0
    student = 0
    for p in sorted(tmp):
        if price+p>b:
            break
        price += p
        student += 1
    max_student = max(max_student, student)

print(max_student)