from sortedcontainers import SortedDict

reverse_sorted_dict = SortedDict(lambda x: -ord(x))

# Add items
reverse_sorted_dict['b'] = 3
reverse_sorted_dict['a'] = 1
reverse_sorted_dict['d'] = 4
reverse_sorted_dict['c'] = 2

print(reverse_sorted_dict)
d = {}
k = d.get(2, [])
print(k)
