import re

n = int(input())
css_lines = [input().strip() for _ in range(n)]

hex_pattern = re.compile(r'(?<!^)\B#([0-9a-fA-F]{6}|[0-9a-fA-F]{3})')

inside_block = False

for line in css_lines:
    line = line.strip()
    
    if '{' in line:
        inside_block = True
    
    if '}' in line:
        inside_block = False

    if inside_block:
        matches = hex_pattern.findall(line)
        for match in matches:
            print('#' + match)