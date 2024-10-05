n = int(input())
arr = [
    int(input())
    for _ in range(n)
]

end_of_range = n

def cut_array(s_idx, e_idx):
    
    global end_of_range, arr

    temp = []
    for i in range(end_of_range):
        if i<s_idx or i>e_idx:
            temp.append(arr[i])

    end_of_range = len(temp)
    for i in range(end_of_range):
        arr[i] = temp[i]

for _ in range(2):
    s, e = map(int, input().split())
    cut_array(s-1, e-1)

print(end_of_range)
for i in range(end_of_range):
    print(arr[i])