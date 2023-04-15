# Enter your code here. Read input from STDIN. Print output to STDOUT
m =  int(input())
setm = set(map(int, input().split(" ")))
n =  int(input())
setn = set(map(int, input().split(" ")))
c = setm.symmetric_difference(setn)
listc = list(c)
listc.sort()
for i in listc:
    print(i)
    
