dice_counting = [0]*7
arr = list(map(int, input().split()))
for i in arr:
    dice_counting[i] += 1
for i,x in enumerate(dice_counting[1:]):
    print(f"{i+1} - {x}")