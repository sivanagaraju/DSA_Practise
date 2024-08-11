def selection_sort(lst):
    for i in range(len(lst)):
        min_index = i
        for j in range(i+1, len(lst)):
            if lst[min_index] >  lst[j]:
                min_index = j
        lst[i] , lst[min_index] = lst[min_index], lst[i]

def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(0, len(lst) - i - 1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                
def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        print("key", key)
        print("j", j)
        while j >=0 and key < lst[j]:
            lst[j+1] = lst[j]
            print("lst[j+1]" , lst[j+1])
            print("list",lst)
            j -= 1
            print("j after -1", j)
        lst[j+1] = key
        print("list out of inner loop", lst)
        

def merge_sort(lst):
    if len(lst) > 1:
        mid = len(lst) // 2
        left = lst[:mid]
        right = lst[mid:]
        
        merge_sort(left)
        merge_sort(right)
        
        i, j, k = 0, 0, 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1
            k += 1
            
        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1
            
        while j < len(right):
            lst[k] = right[j]
            j += 1
            k += 1

def quick_sort(lst):
    if len(lst) < 1 :
        return lst
    else:
        pivot = lst[0]
        less_then_pivot = [x for x in lst[1:] if x <= pivot]
        greater_then_pivot = [x for x in lst[1:] if x > pivot]
        return quick_sort(less_then_pivot) + [pivot] + quick_sort(greater_then_pivot)
             
                
    
        
if __name__ == '__main__':
    lst = [10, 6, 1, 34, 5, 10, -1]
    # selection_sort(lst)
    # print(lst)
    # bubble_sort(lst)
    # print(lst)
    # insertion_sort(lst)
    print(lst)
    merge_sort(lst)
    print(lst)