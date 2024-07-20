import email.utils
import re

n = int(input())

for _ in range(n):
    user, addr = input().split()

    pattern = re.match(r'\<([a-zA-Z][\w\.\-\_]+)@([a-zA-Z]+)\.([a-zA-Z]){1,3}\>$', addr)

    if pattern:
        print(email.utils.formataddr((email.utils.parseaddr(f'{user} {addr}')[0],
                                      email.utils.parseaddr(f'{user} {addr}')[1])))