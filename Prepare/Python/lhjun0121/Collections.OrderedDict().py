from collections import OrderedDict

ordered_dict = OrderedDict()
N = int(input())
for _ in range(N):
    Input = input().split()
    net_price = int(Input.pop())
    item_name = ' '.join(Input)
    if item_name in ordered_dict.keys():
        ordered_dict[item_name] += net_price
    else:
        ordered_dict[item_name] = net_price

for i in ordered_dict.items():
    print(i[0], str(i[1]))