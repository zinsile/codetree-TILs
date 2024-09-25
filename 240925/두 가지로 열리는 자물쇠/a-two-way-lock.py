n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))


mul = 1
for i in range(3):
    posible_ls1, posible_ls2 = [], [] 
    a1,a2 = arr1[i], arr2[i]
    posible_ls1.append(a1)
    posible_ls2.append(a2)
    for j in range(1,3):
        if 0<a1-j<=n:
            posible_ls1.append(a1-j)
        if 0<a1+j<=n:
            posible_ls1.append(a1+j)
        if 0<a2-j<=n:
            posible_ls2.append(a2-j)
        if 0<a2+j<=n:
            posible_ls2.append(a2+j)
        if a1+j>n:
            posible_ls1.append((a1+j)-n)
        if a2+j>n:
            posible_ls2.append((a2+j)-n)
        if 0>=a1-j:
            posible_ls1.append(n+(a1-j))
        if 0>=a2-j:
            posible_ls2.append(n+(a2-j))
    
    sub_mul = 0
    for k in posible_ls1:
        if k in posible_ls2:
            sub_mul += 1
    mul *= sub_mul

print(250-mul)

        
            


















# def match_number(a,b,c):
#     arr = [a,b,c]
#     cnt_1, cnt_2 = 0, 0
#     for i in range(3):
#         if abs(arr[i]-arr1[i]) <= 2 or abs(arr[i]-arr1[i]) == n-2:
#             cnt_1 += 1
#         if abs(arr[i]-arr2[i]) <= 2 or abs(arr[i]-arr2[i]) == n-2:
#             cnt_2 += 1
#     return cnt_1, cnt_2

# result = 0
# for a in range(1,n+1):
#     for b in range(1,n+1):
#         for c in range(1,n+1):
#             cnt1, cnt2 = match_number(a,b,c)
#             if cnt1==3 or cnt2==3:
#                 result+=1

# print(result)