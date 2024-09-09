n,m,k = map(int, input().split())
y_card = [0]*(n+1)
temp = False
for i in range(m):
    num = int(input())
    y_card[num] += 1
    if k in y_card:
        print(y_card.index(k))
        temp = True
        break
if not temp:
    print(-1)