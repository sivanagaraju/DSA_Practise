def square_sort_array(nums):
    # we have to understand new variables have to created and arr list for storing the values
    # how to replace the values in the new list and the position is defined
    # as this is a sorted order we already aware the last will have the highest square
    n = len(nums)
    squares = [0] * n
    left = 0
    right = n - 1
    highest_square_index = n -1
    
    while left <= right:
        left_square = nums[left]**2
        right_square = nums[right]**2
        
        if left_square > right_square: # this works because we mentioned right as last digit of the list
            squares[highest_square_index] = left_square
            left +=1
        else:
            squares[highest_square_index] = right_square
            right -=1
        
        highest_square_index -=1
    return squares


# inplace wont work
def sorted_squares_in_place(num):
    n = len(num)
    left, right = 0, n-1
    
    for i in range(n - 1, -1, -1):
        if abs(num[left]) > abs(num[right]):
            nums.insert(n, nums[left]**2)
            nums.pop(left)
            left+=1
        else:
            nums.insert(n, nums[right]**2)
            nums.pop(right)
            right-=1
    return nums
            

nums = [-4, -1, 0, 3, 10]
print("Sorted squares:", square_sort_array(nums))
# print("Sorted squares in place:", sorted_squares_in_place(nums))
        