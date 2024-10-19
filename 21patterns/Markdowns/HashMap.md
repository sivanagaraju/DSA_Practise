# Comprehensive Guide to Hash Map Pattern 

### 1. Core Concepts and Coding Patterns

Hash Map (or Hash Table) is a data structure that stores key-value pairs and provides efficient lookup, insertion, and deletion operations. The keys are used to index values, making it ideal for scenarios where fast data retrieval is needed.

- **Hashing**: The core concept behind Hash Map is hashing, which involves applying a hash function to the key to determine the index in an underlying array. This ensures  average time complexity for operations.
- **Collisions**: When multiple keys hash to the same index, this is called a collision. Hash Maps handle collisions using methods like chaining (linked lists to store values) or open addressing (finding another index).
- **Typical Use Cases**: Hash Maps are useful for counting frequencies, maintaining mappings, or solving problems involving quick lookups and checking for duplicates.

### 2. Examples

Consider an example where you need to count the occurrence of each number in a list:

```python
arr = [1, 2, 3, 1, 2, 4, 5, 1]
```

Using a Hash Map:

```python
# Resultant Hash Map:
# {
#   1: 3,
#   2: 2,
#   3: 1,
#   4: 1,
#   5: 1
# }
```

Here, the key is each unique number, and the value is the count of its occurrence.

### 3. Problem Identification Checklist

A Hash Map is suitable for problems involving:

| Criteria                     | Example Problem                         |
| ---------------------------- | --------------------------------------- |
| Counting frequencies         | Count character occurrences in a string |
| Maintaining mappings         | Find the first unique character         |
| Tracking index relationships | Two-sum problem                         |

### 4. General Templates with Detailed Comments and Explanations

#### Template 1: Counting Frequencies

```python
# Template to count frequencies of elements in a list.
def count_frequencies(arr):
    # Initialize an empty dictionary to store frequency counts.
    frequency_map = {}
    for num in arr:
        # Check if the current number is already in the map.
        if num in frequency_map:
            # If present, increment the count by 1.
            frequency_map[num] += 1
        else:
            # If not present, add the number to the map with an initial count of 1.
            frequency_map[num] = 1
    # Return the frequency map containing counts of all elements.
    return frequency_map

# Example usage:
arr = [1, 2, 3, 1, 2, 1]
print(count_frequencies(arr))  # Output: {1: 3, 2: 2, 3: 1}
```

- **Use Cases**: This template is useful for counting occurrences in lists or strings, such as counting character frequencies or counting item occurrences in a collection.
- **Complexity**: The time complexity is , where  is the length of the list, and the space complexity is  for storing the frequency counts.

#### Template 2: Using Hash Map to Find Two Numbers that Sum to a Target

```python
# Template to find indices of two numbers that sum up to a given target.
def two_sum(nums, target):
    # Initialize an empty dictionary to store the index of each number encountered.
    index_map = {}  # Key: number, Value: index of the number
    for i, num in enumerate(nums):
        # Calculate the complement that, when added to the current number, equals the target.
        complement = target - num
        # Check if the complement is already in the map.
        if complement in index_map:
            # If complement is found, return the indices of the complement and current number.
            return [index_map[complement], i]
        # Store the current number with its index in the map.
        index_map[num] = i
    # If no such pair is found, return an empty list.
    return []

# Example usage:
nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))  # Output: [0, 1]
```

- **Use Cases**: This template is most applicable for finding pairs with a given sum, such as finding two numbers in an array that add up to a specific value.
- **Complexity**: The time complexity is , where  is the number of elements in the list, and the space complexity is  for storing indices in the map.

#### Template 3: Grouping Elements by Frequency

```python
# Template to group elements by their frequency.
def group_elements_by_frequency(arr):
    # Step 1: Count the frequency of each element.
    frequency_map = {}
    for num in arr:
        if num in frequency_map:
            frequency_map[num] += 1
        else:
            frequency_map[num] = 1

    # Step 2: Group elements by frequency.
    grouped_map = {}  # Key: frequency, Value: list of elements with that frequency
    for num, frequency in frequency_map.items():
        if frequency not in grouped_map:
            grouped_map[frequency] = []
        grouped_map[frequency].append(num)

    return grouped_map

# Example usage:
arr = [1, 2, 3, 1, 2, 1]
print(group_elements_by_frequency(arr))  # Output: {3: [1], 2: [2], 1: [3]}
```

- **Use Cases**: Useful for problems where elements need to be grouped based on their occurrence frequency, such as finding elements that occur the most or least.
- **Complexity**: The time complexity is  for counting and grouping elements, and the space complexity is  for storing both frequency and grouping maps.

### 5. Complexity Analysis

- **Time Complexity**: Operations like lookup, insertion, and deletion have an average complexity of , but can degrade to  in the worst case due to collisions.
- **Space Complexity**: Hash Maps generally require  space for storing key-value pairs.
- **Optimization Opportunities**: Minimizing collisions by choosing an efficient hash function can significantly improve performance.

### 6. Discussion on Templates and Patterns

- Templates like frequency counting or mapping indices are versatile. Adjustments might be needed for specific edge cases, such as when dealing with negative values or non-numeric keys.

### 7. Multiple Approaches and Implementations

#### Iterative Approach

The iterative approach for counting or tracking is efficient in most cases. It involves traversing the list once and updating the Hash Map.

#### Recursive Approach

For problems like DFS that require maintaining a history, recursive Hash Map usage might be suitable but should be used with care due to stack limitations.

| Approach  | Advantages                         | Disadvantages                      |
| --------- | ---------------------------------- | ---------------------------------- |
| Iterative | Easy to implement, efficient       | May require extra state management |
| Recursive | Natural fit for tree-like problems | Higher risk of stack overflow      |

### 8. Practice Problems

| S.No | Question                                       | Example                                                                                                                                                                                                                     | Difficulty Level | Approach                                                                                           |
| ---- | ---------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | -------------------------------------------------------------------------------------------------- |
| 1    | Count character frequencies                    | Given the string "banana", count the frequency of each character. Numeric Example: {'b': 1, 'a': 3, 'n': 2}. Output: {'b': 1, 'a': 3, 'n': 2}                                                                               | Easy             | Use counting frequency template. Variables: frequency\_map. Loop through each character in string. |
| 2    | Two-sum problem                                | Given the list [2, 7, 11, 15] and target = 9, find indices of two numbers that sum to target. Numeric Example: Complement of 2 is 7. Output: [0, 1]                                                                         | Easy             | Use two-sum template. Variables: index\_map. Track complement indices.                             |
| 3    | Find first unique character                    | Given the string "swiss", find the first unique character. Numeric Example: 'w' is the first character with a count of 1. Output: 'w'                                                                                       | Easy             | Use counting frequency template. Track the index of first unique character.                        |
| 4    | Group anagrams                                 | Given a list of strings, group anagrams together. Numeric Example: ['eat', 'tea', 'tan', 'ate', 'nat', 'bat'] -> [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]. Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']] | Medium           | Use sorting and hash map to group strings that have the same sorted form.                          |
| 5    | Subarray sum equals k                          | Find the number of subarrays that sum to k in the list [1, 2, 3, -2, 1, 4, 5]. Numeric Example: Sum of [1, 2, 3, -2, 1] is 5. Output: 2                                                                                     | Medium           | Use prefix sum hash map to track occurrences of sums.                                              |
| 6    | Longest consecutive sequence                   | Given [100, 4, 200, 1, 3, 2], find the length of the longest consecutive elements sequence. Numeric Example: Sequence [1, 2, 3, 4]. Output: 4                                                                               | Medium           | Use hash set to track and find the longest sequence.                                               |
| 7    | Find duplicates in array                       | Find all the duplicates in a list [4, 3, 2, 7, 8, 2, 3, 1]. Numeric Example: Duplicate elements are 2 and 3. Output: [2, 3]                                                                                                 | Easy             | Use counting frequency template to identify elements with count > 1.                               |
| 8    | Top k frequent elements                        | Find the top 2 frequent elements from [1, 1, 1, 2, 2, 3]. Numeric Example: Frequencies are {1: 3, 2: 2, 3: 1}. Output: [1, 2]                                                                                               | Medium           | Use frequency counting and max heap to identify top k elements.                                    |
| 9    | Minimum window substring                       | Given strings "ADOBECODEBANC" and "ABC", find the minimum window that contains all characters of "ABC". Numeric Example: Minimum window is "BANC". Output: "BANC"                                                           | Hard             | Use sliding window with character frequency hash map.                                              |
| 10   | First recurring character                      | Find the first recurring character in the string "abcdefga". Numeric Example: 'a' is the first repeating character. Output: 'a'                                                                                             | Easy             | Use hash map to track first occurrence of each character.                                          |
| 11   | Longest substring without repeating characters | Find the longest substring without repeating characters in "abcabcbb". Numeric Example: "abc" has length 3. Output: "abc"                                                                                                   | Medium           | Use sliding window and hash set to track characters.                                               |
| 12   | Intersection of two arrays                     | Given arrays [1, 2, 2, 1] and [2, 2], find their intersection. Numeric Example: Intersection is [2]. Output: [2]                                                                                                            | Easy             | Use hash map to store counts of elements in one array and find matches in the other.               |
| 13   | Isomorphic strings                             | Determine if two strings "egg" and "add" are isomorphic. Numeric Example: Mapping 'e' to 'a', 'g' to 'd'. Output: True                                                                                                      | Easy             | Use two hash maps to store character mappings between strings.                                     |
| 14   | K-diff pairs in an array                       | Find pairs with difference k = 2 in array [3, 1, 4, 1, 5]. Numeric Example: Pairs are (1, 3) and (3, 5). Output: 2                                                                                                          | Medium           | Use hash map to track occurrences and look for complements.                                        |
| 15   | Maximum size subarray sum equals k             | Given array [1, -1, 5, -2, 3] and k = 3, find the maximum length of a subarray that sums to k. Numeric Example: Maximum length is 4 for subarray [1, -1, 5, -2]. Output: 4                                                  | Medium           | Use prefix sum with hash map to track indices of cumulative sums.                                  |
| 16   | Happy number                                   | Determine if 19 is a happy number. Numeric Example: Sum of squares: 1^2 + 9^2 = 82. Eventually reaches 1. Output: True                                                                                                      | Easy             | Use hash set to track sums of squares and detect cycles.                                           |
| 17   | Longest palindrome substring                   | Find the longest palindromic substring in "babad". Numeric Example: Longest palindromes are "bab" or "aba". Output: "bab" or "aba"                                                                                          | Medium           | Use dynamic programming and hash map to track possible palindromes.                                |
| 18   | Longest harmonious subsequence                 | Find the longest harmonious subsequence in [1, 3, 2, 2, 5, 2, 3, 7]. Numeric Example: Harmonious subsequence is [3, 2, 2, 2, 3]. Output: 5                                                                                  | Medium           | Use hash map to track counts of elements and their neighbors.                                      |
| 19   | Bulls and Cows game                            | Given secret "1807" and guess "7810", calculate bulls and cows. Numeric Example: Bulls = 1 ("8"), Cows = 3 ("7", "1", "0"). Output: "1A3B"                                                                                  | Medium           | Use hash map to track frequency counts of digits for bulls and cows calculation.                   |
| 20   | Word pattern                                   | Check if pattern "abba" matches string "dog cat cat dog". Numeric Example: Mapping pattern 'a' to 'dog' and 'b' to 'cat'. Output: True                                                                                      | Easy             | Use two hash maps to establish mapping between pattern and words.                                  |
| 21   | Subarray sum divisible by k                    | Find the number of subarrays divisible by k = 5 in [4, 5, 0, -2, -3, 1]. Numeric Example: Total subarrays = 7. Output: 7                                                                                                    | Medium           | Use prefix sum with hash map to track modulo results.                                              |
| 22   | Fraction to recurring decimal                  | Convert 4/333 to a recurring decimal. Numeric Example: Decimal is "0.(012)". Output: "0.(012)"                                                                                                                              | Medium           | Use hash map to store remainders to detect cycles.                                                 |
| 23   | Find all anagrams in a string                  | Find all start indices of anagrams of "abc" in "cbaebabacd". Numeric Example: Start indices are [0, 6]. Output: [0, 6]                                                                                                      | Medium           | Use sliding window and character frequency hash map.                                               |
| 24   | Maximum width of binary tree                   | Find the maximum width of a binary tree given its nodes. Numeric Example: Width of binary tree = 4. Output: Integer                                                                                                         | Medium           | Use BFS with hash map to track positions at each level.                                            |
| 25   | Valid Sudoku                                   | Determine if a 9x9 Sudoku board is valid. Numeric Example: Check rows, columns, and 3x3 boxes for duplicates. Output: True/False                                                                                            | Medium           | Use hash map to track rows, columns, and 3x3 sub-boxes.                                            |
| 26   | Continuous subarray sum                        | Given an array, find if there is a subarray with sum that is a multiple of k. Numeric Example: Subarray sum is multiple of k. Output: True                                                                                  | Medium           | Use prefix sum and hash map to track mod values.                                                   |
| 27   | Find duplicate subtrees                        | Find all duplicate subtrees in a binary tree. Numeric Example: List of duplicate root nodes. Output: List of duplicate root nodes                                                                                           | Hard             | Use hash map with serialization to detect duplicates.                                              |
| 28   | Longest repeating character replacement        | Replace characters to get the longest repeating character sequence. Numeric Example: Length of longest sequence = Integer. Output: Integer                                                                                  | Medium           | Use sliding window and hash map to track character counts.                                         |
| 29   | Binary tree vertical order traversal           | Traverse a binary tree vertically and return nodes in each vertical level. Numeric Example: Nodes at each vertical level. Output: List                                                                                      | Hard             | Use BFS with hash map to track nodes in vertical columns.                                          |
| 30   | Find all pairs with a given difference         | Given an array and a difference value, find all unique pairs. Numeric Example: Unique pairs are found. Output: List of pairs                                                                                                | Medium           | Use hash map to track values and find complements.                                                 |

### 9. Key Takeaways, Tips, and Summary

- **Key Takeaways**: Hash Maps provide efficient lookup and insertion capabilities, making them ideal for problems requiring quick access.
- **Practical Tips**: Always handle edge cases, such as collisions or non-unique keys, appropriately.
- **Summary**: Hash Maps are versatile and efficient for a wide range of problems, especially those involving frequency counting, mapping relationships, or finding pairs.

### 10. Common Pitfalls

- **Mistakes to Avoid**: Forgetting to handle key collisions or assuming keys are unique can lead to incorrect results.
- **Troubleshooting Tips**: Use print statements or a debugger to inspect the Hash Map at each step to ensure keys are being added and updated as expected.

Here are detailed explanations for 7 random practice problems from the list:

### 1. Problem 3: Find First Unique Character
**Problem Statement**: Given the string `"swiss"`, find the first unique character.  
**Numeric Example**:
- Input: `"swiss"`
- The character occurrences are: `'s': 3, 'w': 1, 'i': 1`.
- The first character with a count of `1` is `'w'`.
- **Output**: `'w'`.

**Explanation**:
We iterate through the string and use a hash map to count the frequency of each character. After building the frequency map, we iterate again through the string to find the first character with a count of `1`.

**Python Code**:
```python
# Python implementation to find the first unique character.
def first_unique_character(s):
    frequency_map = {}
    # Count frequencies of each character.
    for char in s:
        frequency_map[char] = frequency_map.get(char, 0) + 1
    # Find the first unique character.
    for char in s:
        if frequency_map[char] == 1:
            return char
    return None

s = "swiss"
print(first_unique_character(s))  # Output: 'w'
```

### 2. Problem 4: Group Anagrams
**Problem Statement**: Given a list of strings, group anagrams together.
**Numeric Example**:
- Input: `['eat', 'tea', 'tan', 'ate', 'nat', 'bat']`
- Anagrams are grouped as: `[['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]`
- **Output**: `[['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]`

**Explanation**:
We use a hash map to group words by their sorted form. The sorted form is used as the key, and the values are lists of words that are anagrams.

**Python Code**:
```python
# Python implementation to group anagrams.
def group_anagrams(words):
    anagrams = {}
    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word not in anagrams:
            anagrams[sorted_word] = []
        anagrams[sorted_word].append(word)
    return list(anagrams.values())

words = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
print(group_anagrams(words))  # Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
```

### 3. Problem 6: Longest Consecutive Sequence
**Problem Statement**: Given `[100, 4, 200, 1, 3, 2]`, find the length of the longest consecutive elements sequence.
**Numeric Example**:
- Input: `[100, 4, 200, 1, 3, 2]`
- The longest sequence is `[1, 2, 3, 4]`.
- **Output**: `4`

**Explanation**:
We use a hash set to store the numbers. For each number, if it's the start of a sequence (i.e., `num - 1` is not in the set), we count how long the sequence continues.

**Python Code**:
```python
# Python implementation to find the longest consecutive sequence.
def longest_consecutive(nums):
    num_set = set(nums)
    longest_streak = 0

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak

nums = [100, 4, 200, 1, 3, 2]
print(longest_consecutive(nums))  # Output: 4
```

### 4. Problem 7: Find Duplicates in Array
**Problem Statement**: Find all the duplicates in a list `[4, 3, 2, 7, 8, 2, 3, 1]`.
**Numeric Example**:
- Input: `[4, 3, 2, 7, 8, 2, 3, 1]`
- Duplicate elements are `2` and `3`.
- **Output**: `[2, 3]`

**Explanation**:
We use a hash map to count occurrences of each element. Elements with counts greater than `1` are duplicates.

**Python Code**:
```python
# Python implementation to find duplicates in an array.
def find_duplicates(arr):
    frequency_map = {}
    duplicates = []

    for num in arr:
        frequency_map[num] = frequency_map.get(num, 0) + 1

    for num, count in frequency_map.items():
        if count > 1:
            duplicates.append(num)

    return duplicates

arr = [4, 3, 2, 7, 8, 2, 3, 1]
print(find_duplicates(arr))  # Output: [2, 3]
```

### 5. Problem 8: Top K Frequent Elements
**Problem Statement**: Find the top `2` frequent elements from `[1, 1, 1, 2, 2, 3]`.
**Numeric Example**:
- Input: `[1, 1, 1, 2, 2, 3]`
- Frequencies are: `{1: 3, 2: 2, 3: 1}`
- Top `2` frequent elements are `[1, 2]`.
- **Output**: `[1, 2]`

**Explanation**:
We use a hash map to count frequencies, and a max heap to keep track of the top `k` frequent elements.

**Python Code**:
```python
from collections import Counter
import heapq

# Python implementation to find the top k frequent elements.
def top_k_frequent(nums, k):
    frequency_map = Counter(nums)
    return heapq.nlargest(k, frequency_map.keys(), key=frequency_map.get)

nums = [1, 1, 1, 2, 2, 3]
k = 2
print(top_k_frequent(nums, k))  # Output: [1, 2]
```

### 6. Problem 9: Minimum Window Substring
**Problem Statement**: Given strings `"ADOBECODEBANC"` and `"ABC"`, find the minimum window that contains all characters of `"ABC"`.
**Numeric Example**:
- Input: `"ADOBECODEBANC"`, `"ABC"`
- The minimum window that contains `'A'`, `'B'`, `'C'` is `"BANC"`.
- **Output**: `"BANC"`

**Explanation**:
We use a sliding window approach to adjust the window size dynamically and keep track of the character count needed using a hash map.

**Python Code**:
```python
from collections import Counter

# Python implementation to find the minimum window substring.
def min_window(s, t):
    if not s or not t:
        return ""

    dict_t = Counter(t)
    required = len(dict_t)
    l, r = 0, 0
    formed = 0
    window_counts = {}
    ans = float("inf"), None, None

    while r < len(s):
        char = s[r]
        window_counts[char] = window_counts.get(char, 0) + 1

        if char in dict_t and window_counts[char] == dict_t[char]:
            formed += 1

        while l <= r and formed == required:
            char = s[l]
            if r - l + 1 < ans[0]:
                ans = (r - l + 1, l, r)

            window_counts[char] -= 1
            if char in dict_t and window_counts[char] < dict_t[char]:
                formed -= 1

            l += 1

        r += 1

    return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]

s = "ADOBECODEBANC"
t = "ABC"
print(min_window(s, t))  # Output: "BANC"
```

### 7. Problem 11: Longest Substring Without Repeating Characters
**Problem Statement**: Find the longest substring without repeating characters in `"abcabcbb"`.
**Numeric Example**:
- Input: `"abcabcbb"`
- The longest substring without repeating characters is `"abc"`.
- **Output**: `"abc"`

**Explanation**:
We use a sliding window approach to keep track of the current substring without repeating characters, adjusting the window as we encounter duplicates.

**Python Code**:
```python
# Python implementation to find the longest substring without repeating characters.
def longest_substring_without_repeating(s):
    char_index_map = {}
    left = 0
    max_length = 0
    start = 0

    for right in range(len(s)):
        if s[right] in char_index_map and char_index_map[s[right]] >= left:
            left = char_index_map[s[right]] + 1
        char_index_map[s[right]] = right
        if right - left + 1 > max_length:
            max_length = right - left + 1
            start = left

    return s[start:start + max_length]

s = "abcabcbb"
print(longest_substring_without_repeating(s))  # Output: "abc"
```

These explanations include the problem statement, a detailed numeric example, and Python code implementations for solving each problem.