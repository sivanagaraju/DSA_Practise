**Sliding Window Concept Checklist**

The sliding window technique is commonly used in problems that involve arrays or strings, where you need to process a contiguous subset of elements. It is especially useful for problems involving maximum, minimum, or sum operations over subarrays of a specific length. Below is a checklist to help identify when the sliding window approach is applicable, and a detailed explanation of how to approach these types of problems.

**Example**:

Consider the array `[1, 3, 5, 7, 9, 11]` and a fixed-size sliding window of size `k = 3`. We want to find the maximum sum of any subarray of size `k`.

- **Initial Window** (`left = 0`, `right = 2`): `[1, 3, 5]` → Sum = `1 + 3 + 5 = 9`
- **Slide the Window** (`left = 1`, `right = 3`): Move one position to the right → `[3, 5, 7]` → Sum = `3 + 5 + 7 = 15`
- **Slide Again** (`left = 2`, `right = 4`): Move one more position to the right → `[5, 7, 9]` → Sum = `5 + 7 + 9 = 21`
- **Final Slide** (`left = 3`, `right = 5`): `[7, 9, 11]` → Sum = `7 + 9 + 11 = 27`

The maximum sum of any subarray of size `k` is `27`.

### Checklist to Identify Sliding Window Problems:

| Criteria                          | Description                                                                                           | Example                                                                                                                                                                                                    |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Subarray/Subsequence Search**   | The problem asks for a subarray/subsequence of an array or string.                                    | Find the longest increasing subsequence in an array.  For example, given an array [10, 22, 9, 33, 21, 50, 41, 60, 80], the longest increasing subsequence is [10, 22, 33, 50, 60, 80], with a length of 6. |
| **Contiguous Elements**           | The solution must involve elements that are contiguous.                                               | Find the maximum sum of a contiguous subarray of length `k`.                                                                                                                                               |
| **Fixed or Variable Size Window** | You are interested in finding a fixed size or dynamic length subarray.                                | Find the smallest subarray with a sum greater than or equal to a given value.                                                                                                                              |
| **Max/Min/Sum Property**          | The problem involves finding the maximum, minimum, or sum of values in a subset of elements.          | Find the maximum sum of any subarray of size `k`.                                                                                                                                                          |
| **Optimization Criteria**         | You need to optimize (maximize or minimize) a condition related to the subset of the array or string. | Find the shortest subarray whose sum is greater than or equal to a target value.                                                                                                                           |

### Types of Sliding Window:

| Sliding Window Type             | Description                                            | Example                                                       |
| ------------------------------- | ------------------------------------------------------ | ------------------------------------------------------------- |
| **Fixed-size Sliding Window**   | The size of the window is fixed.                       | Find the maximum sum of any subarray of size `k`.             |
| **Dynamic-size Sliding Window** | The size of the window changes based on the condition. | Find the smallest subarray whose sum is greater than a value. |

### General Templates

1. **Fixed-Size Sliding Window Template**
   - This template is useful when the size of the window is fixed, such as "maximum sum of subarray of length k".
    ```python
    def fixed_size_sliding_window(arr, k):
        # Initialize the maximum sum as 0
        max_sum = 0
        # Calculate the sum of the first 'k' elements (initial window)
        window_sum = sum(arr[:k])
        # Set the initial window sum as the current maximum sum
        max_sum = window_sum

        # Iterate through the rest of the array starting from index 'k'
        for i in range(k, len(arr)):
            # Update the window by adding the next element and removing the leftmost element
            window_sum += arr[i] - arr[i - k]
            # Update the maximum sum if the current window sum is greater
            max_sum = max(max_sum, window_sum)

        # Return the maximum sum found
        return max_sum
    ```

2. **Dynamic-Size Sliding Window Template**

   - This template is useful when the window size needs to change based on a condition, such as "find the smallest subarray with a sum greater than or equal to a given value".

   ```python
   def dynamic_size_sliding_window(arr, target):
       # Initialize the current window sum as 0
       window_sum = 0
       # Initialize the left pointer of the window
       left = 0
       # Initialize the minimum length to infinity
       min_length = float('inf')

       # Expand the window by moving the right pointer
       for right in range(len(arr)):
           # Add the current element to the window sum
           window_sum += arr[right]

           # Shrink the window from the left as long as the window sum is greater than or equal to the target
           while window_sum >= target:
               # Update the minimum length of the subarray
               min_length = min(min_length, right - left + 1)
               # Subtract the element at the left pointer from the window sum
               window_sum -= arr[left]
               # Move the left pointer to the right
               left += 1

       # Return the minimum length found, or 0 if no valid subarray was found
       return min_length if min_length != float('inf') else 0
   ```

   - **Explanation**: The `right` pointer expands the window by moving to the right, while the `left` pointer shrinks the window when the condition is met. This helps in maintaining the minimum length of the subarray with the desired condition.

### Summary

- **Fixed-size Sliding Window**: Used when the window size is fixed, and you need to compute something for all subarrays of that size.
- **Dynamic-size Sliding Window**: Used when the window size changes based on a condition (e.g., sum, distinct elements).

### Tips

- **Sliding Window Template**: For fixed-size windows, maintain the sum or required value as you slide from left to right.
- For dynamic-size windows, use two pointers (`left` and `right`) to adjust the window size based on the condition.
- Practice identifying the problem type based on the keywords like "subarray", "contiguous", "sum", "maximum", or "minimum".

Using the templates provided above can help solve many sliding window problems efficiently. However, each problem may require minor adjustments, especially in the condition used for expanding or shrinking the window.

### Sliding Window Problems and Approaches

| S.No | Question                                                                                 | Numeric Example                                                                       | Difficulty Level | Approach                                                                                                                                                   |
| ---- | ---------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1    | Find the maximum sum of a subarray of length `k`.                                        | Array: `[1, 2, 3, 4, 5, 6, 7, 8, 9]`, `k = 3` → Output: `24` (subarray `[7, 8, 9]`)   | Easy             | Use a fixed-size sliding window to maintain the sum of the subarray, iterate through the array, adding the next element and removing the leftmost element. |
| 2    | Find the smallest subarray with a sum greater than or equal to a given value.            | Array: `[2, 1, 5, 2, 3, 2]`, Target: `7` → Output: `2` (subarray `[5, 2]`)            | Medium           | Use a dynamic-size sliding window, expand the window to reach the target sum, and then shrink it from the left to find the minimum length.                 |
| 3    | Find the longest substring with at most `k` distinct characters.                         | String: `"eceba"`, `k = 2` → Output: `3` (substring `"ece"`)                          | Medium           | Use a dynamic-size sliding window, track character frequencies, and adjust the left pointer when distinct character count exceeds `k`.                     |
| 4    | Find the maximum number of vowels in a substring of length `k`.                          | String: `"abciiidef"`, `k = 3` → Output: `3` (substring `"iii"`)                      | Easy             | Use a fixed-size sliding window to count the number of vowels in the current window and update the maximum count as the window slides.                     |
| 5    | Find the longest subarray with a sum less than or equal to `S`.                          | Array: `[3, 1, 2, 7, 4, 2, 1, 1, 5]`, `S = 8` → Output: `4` (subarray `[3, 1, 2, 1]`) | Medium           | Use a dynamic-size sliding window, expand to add elements to the window, and shrink from the left when the sum exceeds `S` to find the longest subarray.   |
| 6    | Find the shortest subarray with all unique elements.                                     | Array: `[1, 2, 3, 1, 4, 5, 3]` → Output: `4` (subarray `[1, 4, 5, 3]`)                | Hard             | Use a dynamic-size sliding window with a hash set to track unique elements, expanding and shrinking the window to find the shortest valid subarray.        |
| 7    | Find the longest contiguous subarray with an equal number of 0s and 1s.                  | Array: `[0, 1, 0, 1, 1, 0]` → Output: `6` (whole array)                               | Hard             | Use a dynamic-size sliding window and a hashmap to track the difference between the count of 0s and 1s, adjusting pointers to maintain balance.            |
| 8    | Find the minimum number of consecutive cards you need to pick to achieve a target score. | Array: `[5, 1, 3, 7, 9]`, Target: `15` → Output: `2` (subarray `[7, 9]`)              | Medium           | Use a dynamic-size sliding window, expanding until the score is achieved, then shrinking to minimize the subarray length.                                  |
| 9    | Find the smallest window in a string containing all characters of another string.        | String: `"ADOBECODEBANC"`, Pattern: `"ABC"` → Output: `"BANC"`                        | Hard             | Use a dynamic-size sliding window, track character counts with a hashmap, and shrink the window to find the smallest match.                                |
| 10   | Find the longest substring with no more than `k` repeating characters.                   | String: `"aaabbcc"`, `k = 2` → Output: `5` (substring `"aaabb"`)                      | Medium           | Use a dynamic-size sliding window with character frequency counting to ensure no more than `k` repeating characters.                                       |
| 11   | Find the maximum sum of a subarray of at most `k` elements.                              | Array: `[4, 2, 1, 7, 8, 1, 2, 8, 1, 0]`, `k = 3` → Output: `16` (subarray `[7, 8, 1]`)| Easy             | Use a sliding window to compute the sum of the first `k` elements, and slide the window across the array to find the maximum sum.                          |
| 12   | Find the longest subarray where the difference between the maximum and minimum elements is less than `k`. | Array: `[10, 1, 2, 4, 7, 2]`, `k = 5` → Output: `4` (subarray `[2, 4, 7, 2]`) | Hard             | Use a dynamic-size sliding window with two deques to track the minimum and maximum values in the current window, expanding and shrinking as necessary.     |
| 13   | Find the longest substring without repeating characters.                                | String: `"abcabcbb"` → Output: `3` (substring `"abc"`)                                | Medium           | Use a dynamic sliding window to expand with new characters, shrink when duplicates are found, and maintain the maximum length of the substring.            |
| 14   | Find the length of the longest subarray with `k` odd numbers.                            | Array: `[1, 2, 3, 4, 5, 6, 7]`, `k = 3` → Output: `5` (subarray `[1, 2, 3, 4, 5]`)    | Medium           | Use a dynamic sliding window, expand to include elements, and shrink from the left until exactly `k` odd numbers remain, updating the max length.          |
| 15   | Find the longest binary subarray with more 1s than 0s.                                   | Array: `[1, 0, 1, 1, 0, 1, 1, 0, 0, 1]` → Output: `5` (subarray `[1, 1, 0, 1, 1]`)    | Hard             | Use a dynamic-size sliding window to maintain a count of 1s and 0s, expanding and shrinking the window to ensure more 1s than 0s are present.              |