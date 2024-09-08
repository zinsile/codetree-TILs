n = int(input())
score = list(map(float,input().split()))
avg = sum(score)/n
if avg>=4.0:
    grade = "Perfect"
elif 4.0>avg>=3.0:
    grade = 'Good'
elif avg<3.0:
    grade = 'Poor'
print(f"{avg:.1f}")
print(grade)