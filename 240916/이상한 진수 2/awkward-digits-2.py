bina = list(map(int, input()))

def bina_cal(bina:list):
    n= 0
    for i in range(len(bina)):
        n += bina[len(bina)-1-i]*(2**i)
    return n

n = bina_cal(bina)

for idx, i in enumerate(bina):
    bina[idx] = i ^ 1
    n = max(n, bina_cal(bina))
    bina[idx] = bina[idx] ^ 1

if len(bina)==1 and bina[0]==1:
    print(0)
else: print(n)