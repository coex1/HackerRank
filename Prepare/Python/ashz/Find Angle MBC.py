# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

ab = int(input())
bc = int(input())

def arctan_degrees(opposite, adjacent):
    angle_radians = math.atan2(opposite, adjacent)
    angle_degrees = math.degrees(angle_radians)
    return angle_degrees

t = arctan_degrees(ab, bc)

print(str(int(round(t, 0)))+"\u00b0"
