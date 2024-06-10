import re
text = input()
pattern = input()

start = 0
found = False

if len(pattern) == 1:
    for i in text:
        if i == pattern:
            found = True
            print('('+ str(start) + ", "+ str(start) +')')
        start += 1

else:      
    while True:
        m = re.search(pattern, text[start:])
        if m:
            found = True
            start_pos = start + m.start()
            end_pos = start + m.end() - 1 
            print('(' + str(start_pos) + ', ' + str(end_pos) + ')')
            start = end_pos
        else:
            break

if not found:
    print("(-1, -1)")