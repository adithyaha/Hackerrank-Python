# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

s,k = input().split()
s = sorted(s)
out = []
for i in range(1,int(k)+1):
    out+=sorted(combinations(list(s),i))

for i in out:
    print(''.join(i))
