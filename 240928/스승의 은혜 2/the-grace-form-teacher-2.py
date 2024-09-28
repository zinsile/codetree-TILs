n, b = map(int, input().split())
arr = [int(input()) for _ in range(n)]

max_people = 0
for i in range(n):
    arr[i] = arr[i]//2
    price, people = 0, 0
    for j in sorted(arr):
        price += j
        if price<=b:
            people += 1
    max_people = max(max_people, people)
    arr[i] = arr[i]*2

print(max_people)