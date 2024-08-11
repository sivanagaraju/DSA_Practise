def sliding_window(arr, target):
    # Initialize variables
    left = 0  # Left boundary of the sliding window
    min_length = float('inf')  # For minimum length problems (e.g., Minimum Window Substring)
    max_sum = float('-inf')  # For maximum sum problems (e.g., Maximum Sum Subarray)
    window_sum = 0  # Sum of elements within the current window
    window_count = 0  # Count of elements within the current window
    formed = 0  # Number of elements in the window that meet the condition (used in some problems)

    # Create a dictionary to store the frequency of elements
    freq_map = {}  # Used in problems like Minimum Window Substring

    # Iterate through the array
    for right in range(len(arr)):
        # Add the current element to the window
        window_sum += arr[right]  # Update the window sum
        window_count += 1  # Increment the window count
        freq_map[arr[right]] = freq_map.get(arr[right], 0) + 1  # Update the frequency map

        # Shrink the window if conditions are met
        # While loop logic:
        #   - Shrink the window when the conditions are met
        #   - Conditions:
        #     - window_sum >= target: Update min_length or max_sum
        #     - window_count >= target: Update the result
        while left <= right and (window_sum >= target or window_count >= target):
            # Update the result
            min_length = min(min_length, right - left + 1)  # Update minimum length
            max_sum = max(max_sum, window_sum)  # Update maximum sum

            # Remove the leftmost element from the window
            window_sum -= arr[left]  # Subtract the leftmost element from the window sum
            window_count -= 1  # Decrement the window count
            freq_map[arr[left]] -= 1  # Decrement the frequency count
            if freq_map[arr[left]] == 0:
                del freq_map[arr[left]]  # Remove the element from the frequency map if count is 0

            # Move the window to the right
            left += 1  # Increment the left pointer

    # Return the result
    return min_length if min_length != float('inf') else max_sum

# Example usage
arr = [1, 2, 3, 4, 5]
target = 5
result = sliding_window(arr, target)
print("Result:", result)