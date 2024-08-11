# Implement a function that merges two sorted lists of m and n elements respectively, into another sorted list. Name it merge_lists(lst1, lst2).
# Implement a function that merges two sorted lists of m and n elements respectively, into another sorted list. Name it merge_lists(lst1, lst2).
def merge_lists(lst1, lst2):
    i, j = 0,0
    new_list = []
    total_len = len(lst1) + len(lst2)
    while i + j < total_len:
        if i < len(lst1) and j < len(lst2) and lst1[i] < lst2[j]:
            new_list.append(lst1[i])
            i = i + 1
        elif j < len(lst2):
            new_list.append(lst2[j])
            j = j + 1
        else:
            new_list.append(lst1[i])
            i = i + 1
    return new_list

lst1 = [1,3,4,5, 10, 14, 15]
lst2 = [2, 6, 7, 9]

print(merge_lists(lst1, lst2))
