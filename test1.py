def sort_list_without_repeats(intlist):
    return sorted(list(set(intlist)))

mylist = [11, 54, 32,-5, 11, -100, -5, 0, 0, 32, -5, 0, 17]
print(sort_list_without_repeats(mylist))