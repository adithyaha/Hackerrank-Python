# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
setn = set(map(int, input().split()))
b = int(input())
setb = set(map(int, input().split()))
setc = setb.union(setn)
length = len(setc)
print(length)
