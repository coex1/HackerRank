def split_and_join(line):
    line2 = line.split()
    return "-".join(line2)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)