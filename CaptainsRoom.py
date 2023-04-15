# Enter your code here. Read input from STDIN. Print output to STDOUT
k = int(input())
rooms = list(map(int,input().split()))
roomset = set(rooms)

captains_room = (sum(roomset)*k - sum(rooms))//(k-1)
print(captains_room)
