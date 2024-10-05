arr = list(input())

def count(arr):
    t, cnt, result = arr[0], 1, 0
    for i in arr[1:]:
        if i != t:
            if cnt<10:
                result += 2
            else : resut += 3
            t, cnt = i, 1
        if i == t:
            cnt+=1
    if cnt < 10:
        result += 2
    else : result += 3
        
    return result


def simulate():
    min_length = count(arr)
    for _ in range(len(arr)):
        arr.insert(0, arr.pop())
        min_length = min(min_length, count(arr))
    return min_length

ans = simulate()
print(ans)