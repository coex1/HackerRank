import re

N = int(input())

input_line = ''

for _ in range(N):
    line = input()
    input_line += line

input_line = re.sub(r'<!--.*?-->', '', input_line)

tag_pattern = r"<(\w+)(.*?)>"

attr_pattern = r'(\S+)="([^"]*)"'

for tag_match in re.finditer(tag_pattern, input_line):
    tag_name, tag_attrs = tag_match.groups()
    if not tag_attrs.strip().startswith("/"):
        print(tag_name)
        for attr_match in re.finditer(attr_pattern, tag_attrs):
            attr_name, attr_value = attr_match.groups()
            print(f"-> {attr_name} > {attr_value}")