# Enter your code here. Read input from STDIN. Print output to STDOUT

happiness = 0
m, n = map(int, input().split())
array = list(map(int, input().split()))
seta = set(map(int, input().split()))
setb = set(map(int, input().split()))


for i in array:
    if i in seta: 
        happiness += 1
    elif i in setb:
        happiness -= 1
    else:
        continue

print(happiness)
