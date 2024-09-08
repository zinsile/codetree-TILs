n = list(map(int, input()))
num = 0
for i in range(len(n)):
    num = num*2 + n[i]
num *= 17
binary = []
while True:
    if num<2:
        binary.append(num)
        break
    binary.append(num%2)
    num //= 2
for i in binary[::-1]:
    print(i,end='')