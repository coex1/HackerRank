# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

N = int(input())

for _ in range(N):
    s = input()
    # check if valid hex color code
    for i in re.findall(r'(?<!^)\B#([0-9a-fA-F]{6}|[0-9a-fA-F]{3})', s):
        print('#'+i)
