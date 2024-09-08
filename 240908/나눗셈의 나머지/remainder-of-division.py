t = [0]*10
a,b = tuple(map(int,input().split()))
while True:
    a = a//b
    t[a%b] += 1
    if a<=1:
        break
result = 0
for i in t:
    result += i**2
print(result)