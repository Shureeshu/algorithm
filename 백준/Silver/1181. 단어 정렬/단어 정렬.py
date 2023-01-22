import sys
N = int(input())
input_ = sys.stdin
my_dict = {}
for _ in range(N):
    my_value = input_.readline().rstrip()
    my_key = len(my_value)
    my_dict[my_key] = my_dict.get(my_key, set())
    my_dict[my_key].add(my_value)
for my_key in sorted(my_dict.keys()):
    for my_value in sorted(my_dict[my_key]):
        print(my_value)