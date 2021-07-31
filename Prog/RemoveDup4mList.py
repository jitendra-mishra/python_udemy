def removeDup(my_list):
    new_list = []
    for elem in my_list:
        if elem not in new_list:
            new_list.append(elem)
    return new_list

def removeDup1(my_list):
    return list(set(my_list))
a = [1,2,3,4,3,2,1]
print(a)
print(removeDup(a))
print(removeDup1(a))
