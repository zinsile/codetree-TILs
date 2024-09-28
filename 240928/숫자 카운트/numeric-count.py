n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

result = 0

for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):
            if i==j or j==k or i==k:
                continue
            
            temp = True
            for num,c1,c2 in arr:
                x = num//100
                y = num//10%10
                z = num%10

                cnt1,cnt2 = 0,0
                if x==i:
                    cnt1 += 1
                if y==j:
                    cnt1 += 1
                if z==k:
                    cnt1 += 1
                if x==j or x==k:
                    cnt2 += 1
                if y==i or y==k:
                    cnt2 += 1
                if z==i or z==j:
                    cnt2 += 1
                
                if cnt1 != c1 or cnt2 != c2:
                    temp = False
                    break
            if temp:
                result += 1

print(result)