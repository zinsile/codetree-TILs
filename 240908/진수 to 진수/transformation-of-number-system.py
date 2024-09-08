a,b = map(int, input().split())
n = list(map(int,input()))
num = 0
for i in range(len(n)):
    num = num*a + n[i]
bls = []
while True:
    if b==2 and num<2:
        bls.append(num)
        break
    elif b!=2 and num<2:
        break
    bls.append(num%b)
    num //= b
for i in bls[::-1]:
    print(i,end='')