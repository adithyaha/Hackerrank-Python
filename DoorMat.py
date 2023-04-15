# Enter your code here. Read input from STDIN. Print output to STD
    
n, m = input().split(" ")
n = int(n)
m = int(m)

# bottom half after welcome
for i in range(1, int(n/2)+1):
    print((".|."*(2*i-1)).center(m, "-"))

# welcome
print("WELCOME".center(m, "-"))
# top half before welcome
for i in range(int(n/2), 0, -1):
    print((".|."*(2*i-1)).center(m, "-"))
