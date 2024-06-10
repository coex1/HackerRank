import math
ab = int(input())
bc = int(input())
output = math.atan(ab/bc)

print(round(math.degrees(output)),chr(176),sep="")
