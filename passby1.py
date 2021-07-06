my_list = [6,2,8,2]

def multi_by_two(seq):
    for i in range(len(seq)):
        seq[i] *=2

def print_data(seq):
    print(id(seq))
    for elem in seq:
        print(elem)

print(id(my_list))
print_data(my_list)
multi_by_two(my_list)
print(my_list)