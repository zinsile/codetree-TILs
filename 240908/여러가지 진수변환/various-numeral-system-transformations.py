n,b = map(int,input().split())
bls = []
while True:
    if n<2:
        bls.append(n)
        break
    bls.append(n%b)
    n //= b
for i in bls[::-1]:
    print(i,end='')