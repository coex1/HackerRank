import re

def fun(s):
    # return True if s is a valid email, else return False
    a_split = s.split('@')
    if len(a_split) < 2:
        return False
    username = a_split[0]
    w_split = a_split[1].split('.')
    if len(w_split) < 2:
        return False
    website = w_split[0]
    extension = w_split[1]
    
    if re.search(r'^[A-z0-9-_]*$', username) is None or len(username) == 0:
        return False
    if not website.isalnum():
        return False
    if not extension.isalpha() or len(extension) > 3 or len(extension) == 0:
        return False
    return True

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails
