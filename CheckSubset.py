
T = int(input())

# test cases
for i in range(T):
    a = int(input())
    A = set(map(int, input().split()))
    b = int(input())
    B = set(map(int, input().split()))
    
    if (A.union(B) == B) and (A.intersection(B)==A):
        print('True')
    else:
        print('False')
