def max_sub_array_of_size_k(k, arr):
    max_sum, window_sum, = 0, 0
    window_start = 0
    for i in range(len(arr)):
        window_sum += arr[i]
        if i >= k-1:
            max_sum =max(window_sum, max_sum)
            window_sum -= arr[window_start]
            window_start += 1
    return max_sum
        

def main():
  print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])))
  print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])))


main()

"""
Space Complexity --> O(N)
Time Complexity --> O(1)
"""