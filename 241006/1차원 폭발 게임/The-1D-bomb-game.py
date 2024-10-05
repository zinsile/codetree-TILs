n,m = map(int, input().split())
numbers = [
    int(input())
    for _ in range(n)
]

def get_end_idx_of_explosion(start_idx, cur_num):
    for end_idx in range(start_idx+1, len(numbers)):
        if numbers[end_idx] != cur_num:
            return end_idx-1
    return len(numbers)-1

while True:
    did_explode = False

    for curr_idx, number in enumerate(numbers):

        if number == 0:
            continue
        
        end_idx = get_end_idx_of_explosion(curr_idx, number)

        if end_idx-curr_idx+1 >= m:
            did_explode = True
            numbers[curr_idx:end_idx+1] = [0]*(end_idx-curr_idx+1)
    
    numbers = list(filter(lambda x: x > 0, numbers))

    if not did_explode:
        break

print(len(numbers))
for num in numbers:
    print(num)