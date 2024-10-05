arr = list(input())

def count(arr):
    t = 0
    cnt = 0
    for i in arr:
        if i != t:
            cnt+=1
            t = i
    return 2*cnt


def simulate():
    min_length = count(arr)
    for _ in range(len(arr)):
        arr.insert(0, arr.pop())
        min_length = min(min_length, count(arr))
    return min_length

result = simulate()
print(result)