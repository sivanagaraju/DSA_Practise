**Sliding Window Comprehensive Guide for Coding Interviews**

### 1. Core Concepts and Coding Patterns
The **Sliding Window** technique is a common method used to solve problems that involve arrays or lists, particularly when a continuous subarray or subset needs to be examined. The core idea is to maintain a window of elements over the input collection that "slides" from start to end, adjusting as needed to meet specific conditions. This technique is efficient in scenarios where the subarray length is dynamic or fixed and helps reduce the complexity compared to using nested loops.

**Typical Use Cases**:
- Finding the maximum or minimum sum of a subarray of fixed length.
- Finding a subarray that matches a condition (e.g., longest substring without repeating characters).

### 2. Numeric Example
**Example 1**: Finding the maximum sum of a subarray of length 3 in an array.

Given the array `[1, 3, 5, 2, 7, 6, 4]` and a window size of 3, the sliding window moves across the array as follows:
- Window 1: `[1, 3, 5]` - Sum = 9
- Window 2: `[3, 5, 2]` - Sum = 10
- Window 3: `[5, 2, 7]` - Sum = 14 (maximum)
- Window 4: `[2, 7, 6]` - Sum = 15 (maximum)
- Window 5: `[7, 6, 4]` - Sum = 17 (maximum)

The final answer is `17`.

### 3. Problem Identification Checklist
To identify whether a problem can be solved with the sliding window technique, use the following guidelines:

| **Checklist** | **Example Problem** |
|---------------|---------------------|
| Requires processing of contiguous subarrays or substrings | Find the maximum sum of a subarray of length `k`. |
| Involves optimization of a subarray (e.g., maximum, minimum, shortest) | Longest substring with distinct characters. |
| Condition requires window expansion and contraction | Smallest subarray with sum greater than a target. |

### 4. General Templates with Comments

#### Template 1: Fixed-Size Sliding Window
This template is used when the window size is constant.
```python
# Function to find maximum sum of subarray of size k
def max_sum_subarray(arr, k):
    # Initializing variables
    max_sum = 0
    window_sum = 0
    n = len(arr)

    # Calculating the sum of the first window
    for i in range(k):
        window_sum += arr[i]
    max_sum = window_sum

    # Sliding the window over the rest of the array
    for i in range(k, n):
        # Slide the window to the right by subtracting the element going out of the window
        # and adding the element coming into the window
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)
    
    return max_sum
```
**Use Cases**: Finding maximum/minimum sum or average of subarrays of fixed size.

#### Template 2: Dynamic-Size Sliding Window
This template is used when the window size changes dynamically based on a condition.
```python
# Function to find the length of the smallest subarray with sum >= target
def min_length_subarray(arr, target):
    n = len(arr)
    min_length = float('inf')
    window_sum = 0
    left = 0

    # Expanding the window with the right pointer
    for right in range(n):
        window_sum += arr[right]

        # Contract the window until the condition is met
        while window_sum >= target:
            min_length = min(min_length, right - left + 1)
            window_sum -= arr[left]
            left += 1

    return min_length if min_length != float('inf') else 0
```
**Use Cases**: Problems involving finding the shortest or longest subarray that meets certain criteria.

### 5. Complexity Analysis
- **Fixed-Size Sliding Window**:
  - **Time Complexity**: O(n), since each element is processed once.
  - **Space Complexity**: O(1), as no extra space is used.
- **Dynamic-Size Sliding Window**:
  - **Time Complexity**: O(n), each element is added and removed at most once.
  - **Space Complexity**: O(1).
- **Optimization Opportunities**: Ensure the window is adjusted as soon as the condition is met to minimize unnecessary operations.

### 6. Discussion on Templates and Patterns
Sliding Window patterns can be adapted for many types of problems involving contiguous sequences. Adjustments are often needed, such as using hashmaps for character counts in strings or adjusting both pointers in tandem for more complex conditions.

### 7. Multiple Approaches and Implementations
- **Iterative Approach**: Typically used for the sliding window as it allows easy expansion and contraction of the window.
- **Recursive Approach**: Rarely used for sliding window due to stack limitations and complexity in managing window boundaries.

### 8. Practice Problems
| S.No | Question | Example | Difficulty Level | Approach |
|------|----------|---------|------------------|----------|
| 1    | Maximum sum of subarray of size k | Given an array `[1, 2, 3, 4, 5]` and `k=3`, find the maximum sum of any subarray of length `k`. **Output**: `12` (subarray `[3, 4, 5]`). | Easy | Fixed-size window using basic sum update by adding the new element and removing the old element. |
| 2    | Longest substring without repeating characters | Given the string `"abcabcbb"`, find the length of the longest substring without repeating characters. **Output**: `3` (substring `"abc"`). | Medium | Dynamic-size window using a set to track characters and two pointers to expand and shrink the window. |
| 3    | Smallest subarray with sum greater than target | Given an array `[2, 1, 5, 2, 3, 2]` and `target=7`, find the length of the smallest subarray with a sum greater than `7`. **Output**: `2` (subarray `[5, 3]`). | Medium | Dynamic-size window with left and right pointers to expand and contract, maintaining a running sum. |
| 4    | Longest subarray with at most K distinct characters | Given the string `"eceba"` and `k=2`, find the length of the longest subarray with at most 2 distinct characters. **Output**: `3` (substring `"ece"`). | Hard | Dynamic-size window using a hashmap to track character frequencies and count distinct characters. |
| 5    | Minimum window substring | Given the string `"ADOBECODEBANC"` and target string `"ABC"`, find the minimum window that contains all characters of the target. **Output**: `"BANC"`. | Hard | Dynamic-size window using hashmap to track the frequency of target characters and maintain coverage. |
| 6    | Longest substring with at most two distinct characters | Given the string `"ccaabbb"`, find the length of the longest substring with at most two distinct characters. **Output**: `5` (substring `"aabbb"`). | Medium | Dynamic-size window with a hashmap to track frequencies of characters and ensure at most two distinct ones are present. |
| 7    | Find all anagrams in a string | Find all starting indices of anagrams of the string `"abc"` in `"cbaebabacd"`. **Output**: `[0, 6]`. | Medium | Dynamic-size window with a hashmap to track character counts and compare with the target frequency. |
| 8    | Longest repeating character replacement | Given the string `"AABABBA"` and `k=1`, find the length of the longest substring after replacing at most `k` characters to make all characters the same. **Output**: `4` (substring `"AABA"` or `"ABBA"`). | Medium | Dynamic-size window while keeping track of the most frequent character count in the current window. |
| 9    | Subarrays with K different integers | Given the array `[1, 2, 1, 2, 3]` and `k=2`, find the number of subarrays with exactly `k` different integers. **Output**: `7`. | Hard | Dynamic-size window with two pointers and two hashmaps to maintain and count distinct integers. |
| 10   | Longest substring with at most K distinct vowels | Given the string `"aeiouxxaeiouy"` and `k=3`, find the length of the longest substring with at most `k` distinct vowels. **Output**: `7` (substring `"aeiouxx"`). | Hard | Dynamic-size window using a set to track vowels and a count of distinct vowels in the current window. |
| 11   | Maximum number of vowels in a substring of given length | Given the string `"abciiidef"` and `k=3`, find the maximum number of vowels in any substring of length `k`. **Output**: `3` (substring `"iii"`). | Medium | Fixed-size window to count vowels in the first window and update the count as the window slides. |
| 12   | Longest continuous subarray with absolute difference <= limit | Given the array `[8, 2, 4, 7]` and `limit=4`, find the length of the longest continuous subarray with an absolute difference less than or equal to `4`. **Output**: `2` (subarray `[2, 4]` or `[4, 7]`). | Medium | Dynamic-size window using two deques to maintain the maximum and minimum elements efficiently. |
| 13   | Max consecutive ones III | Given the binary array `[1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1]` and `k=2`, find the length of the longest subarray containing `1`s after flipping at most `k` zeroes. **Output**: `8`. | Medium | Dynamic-size window keeping track of zero count to ensure it doesn't exceed `k`. |
| 14   | Sliding window maximum | Given the array `[1,3,-1,-3,5,3,6,7]` and `k=3`, find the maximum value in each sliding window of size `k`. **Output**: `[3, 3, 5, 5, 6, 7]`. | Hard | Fixed-size window using deque to maintain indices of maximum elements efficiently. |
| 15   | Longest subarray with sum at most K | Given the array `[1, 2, 3, 4, 5]` and `k=10`, find the length of the longest subarray with a sum less than or equal to `10`. **Output**: `4` (subarray `[1, 2, 3, 4]`). | Medium | Dynamic-size window with left and right pointers to maintain the current sum. |
| 16   | Maximum sum of two non-overlapping subarrays | Given the array `[0,6,5,2,2,5,1,9,4]`, `firstLen=1`, `secondLen=2`, find the maximum sum of two non-overlapping subarrays. **Output**: `20` (subarrays `[9]` and `[6, 5]`). | Hard | Sliding window with prefix sums to track and optimize non-overlapping subarray sums. |
| 17   | Count number of nice subarrays | Given the array `[1,1,2,1,1]` and `k=3`, find the number of subarrays with exactly `k` odd numbers. **Output**: `2`. | Medium | Dynamic-size window using two pointers and counting odd numbers in the current window. |
| 18   | Number of subarrays of size K and average greater than or equal to threshold | Given the array `[2,1,3,4,1]`, `k=3`, and `threshold=3`, find the number of subarrays of size `k` with an average greater than or equal to the threshold. **Output**: `1`. | Medium | Fixed-size window calculating the sum and updating it as the window slides. |
| 19   | Shortest subarray with sum at least K | Given the array `[1, 2, 3, 4, 5]` and `k=11`, find the length of the shortest subarray with a sum greater than or equal to `11`. **Output**: `3` (subarray `[3, 4, 5]`). | Hard | Dynamic-size window using deque to maintain the current sum and minimize the window size. |
| 20   | Maximum number of non-overlapping subarrays with sum equals target | Given the array `[1,1,1,1,1]` and `target=2`, find the maximum number of non-overlapping subarrays with a sum equal to `2`. **Output**: `2`. | Hard | Sliding window with greedy approach to track non-overlapping subarrays. |
| 21   | Shortest subarray with sum exactly K | Given the array `[1, 2, -1, 4, -2, 3]` and `k=5`, find the shortest subarray with a sum exactly equal to `5`. **Output**: `2` (subarray `[2, 3]`). | Hard | Dynamic-size window adjusting the sum and minimizing the length of the subarray. |
| 22   | Longest subarray with binary ones | Given the binary array `[0,1,1,1,0,1,1,0,1]`, find the length of the longest subarray containing only `1`s. **Output**: `3`. | Medium | Dynamic-size window keeping track of zero count to ensure the window contains only `1`s. |
| 23   | Longest substring with at least K repeating characters | Given the string `"aaabb"` and `k=3`, find the length of the longest substring in which each character appears at least `k` times. **Output**: `3` (substring `"aaa"`). | Hard | Dynamic-size window to expand and ensure character frequency meets the condition. |

### 9. Key Takeaways, Tips, and Summary
- **Key Takeaways**: Sliding Window is best suited for contiguous subarray/substring problems where optimization or condition-checking is involved.
- **Practical Tips**: Start with the simplest window and adjust dynamically; understand the problem requirements thoroughly.
- **Summary**: Sliding Window is an efficient approach that reduces nested loops into linear time solutions by maintaining a moving subarray.

### 10. Common Pitfalls
- **Mistakes to Avoid**: Forgetting to shrink the window properly, resulting in incorrect answers or infinite loops.
- **Troubleshooting Tips**: Always check boundary conditions, especially when moving the `left` pointer in dynamic-size windows.



### Explanation for "Longest Substring with at most K Distinct Vowels"

**Problem Statement**:
Given a string, you need to find the longest substring that contains at most `K` distinct vowels. 

**Example**:
Given the string `"aeiouxxaeiouy"` and `K = 3`, you want to find the length of the longest substring that contains no more than 3 distinct vowels.

**Output**: `7` (substring `"aeiouxx"`)

The substring `"aeiouxx"` has 3 distinct vowels (`a, e, i`) and is the longest such substring within the given string.

**Approach**:
This problem can be efficiently solved using a dynamic sliding window approach, where two pointers (`left` and `right`) are used to maintain a window over the input string. We use a set or a hashmap to keep track of the distinct vowels in the current window, expanding the window with the right pointer and contracting from the left when the number of distinct vowels exceeds `K`.

**Python Code with Comments**:
```python
def longest_substring_k_vowels(s, k):
    # Initialize pointers and variables
    left = 0
    max_length = 0
    vowel_count = {}
    
    vowels = set('aeiou')
    
    # Iterate over the string with the right pointer
    for right in range(len(s)):
        char = s[right]
        
        # If the character is a vowel, add it to the count dictionary
        if char in vowels:
            if char not in vowel_count:
                vowel_count[char] = 0
            vowel_count[char] += 1
        
        # Check if the number of distinct vowels exceeds k
        while len(vowel_count) > k:
            left_char = s[left]
            if left_char in vowel_count:
                vowel_count[left_char] -= 1
                # Remove from dictionary if count reaches zero
                if vowel_count[left_char] == 0:
                    del vowel_count[left_char]
            left += 1  # Contract the window from the left

        # Update the maximum length of the window
        max_length = max(max_length, right - left + 1)

    return max_length

# Example usage
s = "aeiouxxaeiouy"
k = 3
print(longest_substring_k_vowels(s, k))  # Output: 7
```

The approach ensures that we efficiently find the longest substring by expanding and contracting the window, avoiding unnecessary nested loops.


### Explanation for "Max Consecutive Ones III"

**Problem Statement**:
You are given a binary array (an array consisting of only `0`s and `1`s) and an integer `k`. You need to find the length of the longest subarray that contains only `1`s after flipping at most `k` zeroes.

**Example**:
Given the binary array `[1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1]` and `k = 2`, you want to find the length of the longest subarray that contains only `1`s after flipping at most `2` zeroes.

**Output**: `8`

The longest subarray that meets the condition is `[1, 1, 1, 1, 1, 1, 1, 1]`, which can be obtained by flipping two `0`s to `1`s.

**Approach**:
To solve this problem efficiently, we can use a sliding window approach with two pointers (`left` and `right`). We expand the window by moving the `right` pointer and count how many `0`s are in the current window. If the count of `0`s exceeds `k`, we shrink the window by moving the `left` pointer until the count is `<= k`. This approach ensures that we find the longest window that satisfies the condition.

**Python Code with Explanation**:
```python
def longest_ones(arr, k):
    # Initialize pointers and variables
    left = 0
    max_length = 0
    zero_count = 0

    # Expand the window with the right pointer
    for right in range(len(arr)):
        # If the current element is 0, increment the zero count
        if arr[right] == 0:
            zero_count += 1

        # If the number of zeros exceeds k, shrink the window from the left
        while zero_count > k:
            if arr[left] == 0:
                zero_count -= 1
            left += 1  # Move the left pointer to the right to shrink the window

        # Update the maximum length of the window that contains at most k zeros
        max_length = max(max_length, right - left + 1)

    return max_length

# Example usage
arr = [1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1]
k = 2
print(longest_ones(arr, k))  # Output: 8
```

This approach has a time complexity of `O(n)` since each element is processed at most twice (once by the `right` pointer and once by the `left` pointer), and a space complexity of `O(1)` as it uses only a fixed amount of extra space.

### Explanation for "Longest Substring Without Repeating Characters"

**Problem Statement**:
You are given a string, and you need to find the length of the longest substring that contains no repeating characters.

**Example**:
For the string `"abcabcbb"`, you want to find the length of the longest substring that has no repeating characters.

**Output**: `3`

The longest substring without repeating characters is `"abc"`, which has a length of `3`.

**Approach**:
To solve this problem, we can use a sliding window approach with two pointers (`left` and `right`). We expand the window by moving the `right` pointer and add characters to a set to keep track of the unique characters in the current window. If a character is repeated, we move the `left` pointer to remove characters from the set until there are no more duplicates.

**Python Code with Explanation**:
```python
def longest_substring_without_repeating(s):
    # Initialize pointers and a set to track unique characters
    left = 0
    max_length = 0
    char_set = set()

    # Iterate with the right pointer over the string
    for right in range(len(s)):
        # If the character at the right pointer is already in the set, move the left pointer to remove duplicates
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        # Add the character at the right pointer to the set
        char_set.add(s[right])

        # Update the maximum length of the window
        max_length = max(max_length, right - left + 1)

    return max_length

# Example usage
s = "abcabcbb"
print(longest_substring_without_repeating(s))  # Output: 3
```

This approach has a time complexity of `O(n)` because each character is processed at most twice (once by the `right` pointer and once by the `left` pointer) and a space complexity of `O(min(n, m))`, where `n` is the length of the string and `m` is the size of the character set, due to the usage of the set to track unique characters.

