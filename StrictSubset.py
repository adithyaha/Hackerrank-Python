A = set(map(int, input().split()))
n = int(input())
flag = 0

for i in range(n):
    B = set(map(int, input().split()))
    if len(B)>len(A):
        break
    else:
        if A.intersection(B) == B:
            if A != B:
                flag = 1
        else:
            flag = 0
            break

if flag == 1:
    print('True')
else:
    print('False')
