# 변수 선언 및 입력:
x, y = tuple(map(int, input().split()))
ans = 0

# 각 정수에 대해 
# 팰린드롬 수인지 아닌지 여부를 판단합니다.
for i in range(x, y + 1):
    # 정수 형태를 문자열 배열로 바꿉니다.
    str_i = str(i)

    # 펠린드롬 수가 되기 위해서는,
    # 거꾸로 읽어도 똑같은 수여야 합니다.
    if str_i == str_i[::-1]:
        ans += 1

print(ans)