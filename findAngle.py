# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
AB = int(input())
BC = int(input())

angle = math.atan(AB/BC)
print(str(round(math.degrees(angle)))+'\u00B0')
