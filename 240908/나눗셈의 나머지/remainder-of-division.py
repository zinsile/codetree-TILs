t = [0]*10
a,b = tuple(map(int,input().split()))
while True:
    if a<=1:
        break
    a = a//b
    t[a%b] += 1
result = 0
for i in t:
    result += i**2
print(result)