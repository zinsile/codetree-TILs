m1,d1,m2,d2 = map(int, input().split())
day = input()
day1 = 1

if day == 'Mon': day = 1
elif day == 'Tue': day = 2
elif day == 'Wed': day = 3
elif day == 'Thu': day = 4
elif day == 'Fri': day = 5
elif day == 'Sat': day = 6
elif day == 'Sun': day = 0


months = [31,29,31,30,31,30,31,31,30,31,30,31]
dn1, dn2 = d1, d2
for i in range(m1-1):
    dn1 += months[i]
for i in range(m2-1):
    dn2 += months[i]

day2 = (dn2-dn1)%7

# 만약 day2-day1이 day보다 작으면 0
# 만약 day가 day2보다 작으면 //7
# 만약 day가 day2 같거나 크면 //7 +1
if day2-day1 < day:
    result = 0
elif day < day2:
    result = (dn2-dn1)//7
elif day >= day2:
    result = (dn2-dn1)//7 + 1
print(result)