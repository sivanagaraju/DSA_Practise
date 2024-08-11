def remove_even(lst):
    for val in lst:
        if val % 2 != 0:
            lst.remove(val)
    print(lst)

lst = [1, 2, 4, 3, 5, 7]
remove_even(lst)