m1,d1,m2,d2 = map(int, input().split())
months = [31,28,31,30,31,30,31,31,30,31,30,31]
days = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

day1, day2 = d1, d2

for i in range(m1-1):
    day1 += months[i]
    
for i in range(m2-1):
    day2 += months[i]

result = (day2-day1)%7
print(days[result])