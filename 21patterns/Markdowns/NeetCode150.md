## **ARRAYS & HASHING**

### Problem 1: Contains Duplicate

#### Problem Understanding:

- **Problem Explanation**: The task is to determine if a given array contains any duplicates. Specifically, we need to return `True` if any value appears at least twice in the array, and `False` if every element is distinct.

**Example**:
Input: `[1, 2, 3, 1]`
Output: `True` (because the number 1 appears twice).

#### Coding Pattern:

- The appropriate coding pattern here is **Hashing** (or **Set Usage**). This is because we need to quickly check if we've already seen a value before. By using a set, we can keep track of the elements we encounter in the array. If we find an element that is already in the set, we return `True` immediately. Otherwise, after iterating through the array, we return `False`.

#### Solution:

```python
def contains_duplicate(nums):
    # Initialize an empty set to store unique elements
    seen = set()
  
    # Iterate through each number in the list
    for num in nums:
        # If the current number is already in the set, it means we found a duplicate
        if num in seen:
            return True  # Return True as soon as we find a duplicate
      
        # Add the number to the set if it's not already present
        seen.add(num)
  
    # If no duplicates were found after iterating through the list, return False
    return False

# Time Complexity: O(n) - we traverse the list once
# Space Complexity: O(n) - we use a set to store the numbers

# Test the function with the example
print(contains_duplicate([1, 2, 3, 1]))  # Output: True
```

**Explanation**:

1. We use a **set** because checking membership in a set is O(1) on average.
2. We loop through the array:
   - If we encounter a number that is already in the set, we immediately return `True`.
   - If it's not in the set, we add it to the set.
3. If we finish the loop without finding any duplicates, we return `False`.

#### Alternative Approach:

- Another approach could be sorting the array and then checking adjacent elements for duplicates. However, this is less efficient since sorting takes O(n log n) time.

```python
def contains_duplicate_alternative(nums):
    # Sort the array in-place, so duplicate elements will be adjacent
    nums.sort()
  
    # Check each pair of adjacent elements in the sorted list
    for i in range(1, len(nums)):
        # If any pair of adjacent elements are the same, a duplicate is found
        if nums[i] == nums[i - 1]:
            return True  # Return True if a duplicate is found
  
    # If no duplicates are found after checking all pairs, return False
    return False

# Time Complexity: O(n log n) - due to sorting
# Space Complexity: O(1) - no additional space is used apart from the input list

# Test the alternative function
print(contains_duplicate_alternative([1, 2, 3, 1]))  # Output: True
```

**Explanation**:

- Here, we sort the array first, which takes O(n log n) time.
- Then, we check adjacent elements in the sorted array. If any two adjacent elements are the same, we return `True`.

---

### Problem 2: Valid Anagram

#### Problem Understanding:

- **Problem Explanation**: The task is to determine if two strings are anagrams of each other. Two strings are anagrams if they contain the same characters, with the same frequencies, but possibly in a different order.

**Example**:
Input: `s = "anagram", t = "nagaram"`
Output: `True` (since both strings contain the same letters in any order).

#### Coding Pattern:

- This problem fits well with the **Hashing** or **Frequency Counting** pattern. We can use a dictionary (or an array for constant-size alphabets) to count the frequency of each character in the strings, and then compare these frequencies.

#### Solution:

```python
def is_anagram(s, t):
    # If the two strings have different lengths, they can't be anagrams
    if len(s) != len(t):
        return False
  
    # Dictionary to count the frequency of characters in the first string
    count = {}
  
    # Count the frequency of each character in the first string
    for char in s:
        count[char] = count.get(char, 0) + 1  # Increment the count for each character
  
    # Iterate through the second string
    for char in t:
        if char in count:
            count[char] -= 1  # Decrement the count for each character
            # If the count goes to zero, we remove the character from the dictionary
            if count[char] == 0:
                del count[char]
        else:
            return False  # If a character is not in the dictionary, it's not an anagram
  
    # If the dictionary is empty, both strings are anagrams
    return len(count) == 0

# Time Complexity: O(n) - where n is the length of the strings
# Space Complexity: O(1) - the space required for the dictionary is constant for 26 letters

# Test the function with the example
print(is_anagram("anagram", "nagaram"))  # Output: True

```

**Explanation**:

1. We first check if the lengths of the strings are equal. If not, they cannot be anagrams.
2. We use a dictionary to count the frequency of characters in the first string.
3. Then, for the second string, we decrease the count of the characters in the dictionary. If any character does not exist or the counts don't match, we return `False`.
4. If we finish and the dictionary is empty, the strings are anagrams.

---

### Problem 3: Two Sum

#### Problem Understanding:

- **Problem Explanation**: You are given an array of integers and a target integer. The task is to find two distinct indices such that the sum of the numbers at those indices is equal to the target.

**Example**:
Input: `nums = [2, 7, 11, 15]`, `target = 9`
Output: `[0, 1]` (since nums[0] + nums[1] = 9).

#### Coding Pattern:

- The **Hashing** pattern works well here. We can keep track of the complement (target - current element) in a dictionary while iterating through the list. If we encounter an element that is already in the dictionary (i.e., its complement was seen earlier), we return the indices.

#### Solution:

```python
def two_sum(nums, target):
    # Dictionary to store the complement (target - num) and its index
    complement_map = {}
  
    # Iterate over the list with both index and value
    for i, num in enumerate(nums):
        complement = target - num  # Calculate the complement that adds up to the target
      
        # Check if the complement exists in the dictionary (i.e., we've seen it before)
        if complement in complement_map:
            # Return the index of the complement and the current index
            return [complement_map[complement], i]
      
        # Otherwise, store the current number's index in the dictionary
        complement_map[num] = i
  
    # In case no solution exists, return an empty list
    return []

# Time Complexity: O(n) - we traverse the list once
# Space Complexity: O(n) - we use a dictionary to store the complements and their indices

# Test the function with the example
print(two_sum([2, 7, 11, 15], 9))  # Output: [0, 1]
```

#### Alternative Approach:

An alternative approach involves **brute force**, where we check every pair of elements and return the indices if their sum matches the target. This method is simple but inefficient for large inputs.

```python
def two_sum_brute_force(nums, target):
    # Iterate over each pair of numbers in the list
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            # If the sum of the two numbers equals the target, return their indices
            if nums[i] + nums[j] == target:
                return [i, j]
  
    # In case no solution exists, return an empty list
    return []

# Time Complexity: O(n^2) - we check every pair of numbers
# Space Complexity: O(1) - no extra space is used apart from the indices

# Test the function with the example
print(two_sum_brute_force([2, 7, 11, 15], 9))  # Output: [0, 1]

```

**Note**: The brute-force approach is slower, with a time complexity of **O(n²)**, compared to the more efficient hashing approach, which has **O(n)** time complexity.

---

### Problem 4: Group Anagrams

#### Problem Understanding:

- **Problem Explanation**: Given an array of strings, group the anagrams together. Anagrams are strings made up of the same characters with the same frequencies, but possibly in different orders.

**Example**:
Input: `["eat", "tea", "tan", "ate", "nat", "bat"]`
Output: `[['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]`

#### Coding Pattern:

- The appropriate pattern is **Hashing**. By using a dictionary where the keys are sorted versions of the words (or frequency counts), and the values are lists of words that match that key, we can easily group the anagrams.

#### Solution:

```python
def group_anagrams(strs):
    # Dictionary to group words by their sorted character tuple
    anagram_map = {}
  
    # Iterate through each word in the input list
    for word in strs:
        # Sort the characters in the word to form a key
        key = tuple(sorted(word))
      
        # Add the word to the list corresponding to the sorted key in the dictionary
        if key not in anagram_map:
            anagram_map[key] = []
        anagram_map[key].append(word)
  
    # Return the values (grouped anagrams) as a list of lists
    return list(anagram_map.values())

# Time Complexity: O(n * k log k) - where n is the number of words and k is the average length of the word (sorting each word)
# Space Complexity: O(n * k) - space needed to store the words and their corresponding sorted keys

# Test the function with the example
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))  
# Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
```

#### Alternative Approach:

Another approach could be using **character frequency** as the key instead of sorting. Instead of sorting the string, we count the frequency of each character and use the frequency tuple as the key.

```python
def group_anagrams_alternative(strs):
    # Dictionary to group words by their character frequency tuple
    anagram_map = {}
  
    # Iterate through each word in the input list
    for word in strs:
        # Create a list of 26 zeros to represent the frequency of each character
        count = [0] * 26
      
        # Count the frequency of each character in the word
        for char in word:
            count[ord(char) - ord('a')] += 1
      
        # Use the tuple of counts as the key
        key = tuple(count)
      
        # Add the word to the corresponding list in the dictionary
        if key not in anagram_map:
            anagram_map[key] = []
        anagram_map[key].append(word)
  
    # Return the values (grouped anagrams) as a list of lists
    return list(anagram_map.values())

# Time Complexity: O(n * k) - n is the number of words, and k is the max length of a word (counting each character)
# Space Complexity: O(n * k) - space needed to store the words and their corresponding frequency counts

# Test the function with the example
print(group_anagrams_alternative(["eat", "tea", "tan", "ate", "nat", "bat"]))  
# Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

```

**Note**: This approach avoids sorting the string and may perform better when the strings are long, but its complexity depends on the number of characters (26 for lowercase letters).

---

### Problem 5: Top K Frequent Elements

#### Problem Understanding:

- **Problem Explanation**: Given an integer array, return the k most frequent elements.

**Example**:
Input: `nums = [1, 1, 1, 2, 2, 3]`, `k = 2`
Output: `[1, 2]` (since 1 appears 3 times, 2 appears 2 times).

#### Coding Pattern:

- The pattern to solve this problem is **Heap** or **Bucket Sort**. We can either use a max-heap to keep track of the top k elements, or use bucket sort if the number of unique elements is small compared to the array size.

#### Solution (Heap-based):

```python
import heapq
from collections import Counter

def top_k_frequent(nums, k):
    # Create a frequency map of elements in the list
    count = Counter(nums)
  
    # Use a heap to get the k most frequent elements
    # 'nlargest' returns the k largest elements based on their frequency count
    return heapq.nlargest(k, count.keys(), key=count.get)

# Time Complexity: O(n log k) - counting is O(n), and extracting k elements from the heap is O(log k)
# Space Complexity: O(n) - for storing the frequency count

# Test the function with the example
print(top_k_frequent([1, 1, 1, 2, 2, 3], 2))  # Output: [1, 2]

```

#### Alternative Approach (Bucket Sort):

```python
from collections import defaultdict

def top_k_frequent_bucket(nums, k):
    # Frequency map to count occurrences of each number
    freq_map = defaultdict(int)
  
    # Count the frequency of each number in the input list
    for num in nums:
        freq_map[num] += 1
  
    # Create buckets: each index represents a frequency, and the value is a list of numbers
    bucket = [[] for _ in range(len(nums) + 1)]
  
    # Populate the bucket based on the frequency of each number
    for num, freq in freq_map.items():
        bucket[freq].append(num)
  
    # Gather the k most frequent elements
    result = []
  
    # Traverse the bucket from the highest frequency to the lowest
    for i in range(len(bucket) - 1, 0, -1):
        for num in bucket[i]:
            result.append(num)
            # If we've collected k elements, return the result
            if len(result) == k:
                return result

# Time Complexity: O(n) - for counting and bucket sorting
# Space Complexity: O(n) - for storing the frequency map and buckets

# Test the function with the example
print(top_k_frequent_bucket([1, 1, 1, 2, 2, 3], 2))  # Output: [1, 2]
```

---

### Problem 6: Encode and Decode Strings

#### Problem Understanding:

- **Problem Explanation**: The task is to encode a list of strings into a single string and then decode that string back into the original list of strings. We need a reliable method to ensure that when we decode the string, it splits the original list correctly (even if there are special characters like commas or spaces in the strings).

**Example**:
Input: `["lint", "code", "love", "you"]`
Encoded Output: `"4#lint4#code4#love3#you"`
Decoded Output: `["lint", "code", "love", "you"]`

#### Coding Pattern:

- This problem can be solved using **custom encoding**. We encode the length of each string followed by a delimiter (`#`) and the actual string. When decoding, we extract the length and retrieve the corresponding substring.

#### Solution:

```python
def encode(strs):
    """
    Encodes a list of strings to a single string.
    """
    encoded_str = ""
  
    # Iterate through each string in the list
    for s in strs:
        # For each string, prepend its length followed by a delimiter '#'
        encoded_str += str(len(s)) + '#' + s
  
    return encoded_str

def decode(encoded_str):
    """
    Decodes a single string to a list of strings.
    """
    decoded_strs = []
    i = 0
  
    # Iterate through the encoded string
    while i < len(encoded_str):
        # Find the position of the delimiter '#' to get the length of the next string
        j = encoded_str.index('#', i)
        length = int(encoded_str[i:j])  # Convert the substring (length) to an integer
        i = j + 1  # Move past the delimiter
      
        # Extract the actual string using the length we just decoded
        decoded_strs.append(encoded_str[i:i + length])
      
        # Move the index to the start of the next encoded part
        i += length
  
    return decoded_strs

# Time Complexity: O(n) - where n is the total length of all the strings combined (for both encode and decode)
# Space Complexity: O(n) - we use extra space for the encoded string and decoded list

# Test the functions
encoded = encode(["lint", "code", "love", "you"])
print(encoded)  # Output: "4#lint4#code4#love3#you"
decoded = decode(encoded)
print(decoded)  # Output: ["lint", "code", "love", "you"]
```

#### Alternative Approach:

- **No alternative approach** for this encoding and decoding method is required, as this custom encoding method efficiently solves the problem.

---

### Problem 7: Product of Array Except Self

#### Problem Understanding:

- **Problem Explanation**: Given an array of integers, return an array such that each element at index `i` is the product of all numbers in the array except the one at index `i`. You cannot use division, and the time complexity must be O(n).

**Example**:
Input: `[1, 2, 3, 4]`
Output: `[24, 12, 8, 6]` (since 24 = 2\*3\*4, 12 = 1\*3\*4, etc.)

#### Coding Pattern:

- This problem can be solved using the **prefix and suffix product** pattern. We calculate two arrays: the product of all elements to the left of the current element (prefix product) and the product of all elements to the right (suffix product). We then multiply these two for each element.

#### Solution:

```python
def product_except_self(nums):
    n = len(nums)
  
    # Initialize the result array with 1's to store the final products
    result = [1] * n
  
    # Step 1: Calculate prefix products (product of all elements to the left)
    prefix = 1
    for i in range(n):
        result[i] = prefix  # Store the prefix product
        prefix *= nums[i]   # Update the prefix for the next element
  
    # Step 2: Calculate suffix products (product of all elements to the right)
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix  # Multiply the stored prefix product with the suffix product
        suffix *= nums[i]    # Update the suffix for the next element
  
    return result

# Time Complexity: O(n) - we traverse the array twice (once for prefix, once for suffix)
# Space Complexity: O(1) - we use constant space for the result, not counting the output array

# Test the function with the example
print(product_except_self([1, 2, 3, 4]))  # Output: [24, 12, 8, 6]
```

#### Alternative Approach:

- **No alternative approach** is needed, as this method avoids division and meets the O(n) time complexity requirement.

---

### Problem 8: Valid Sudoku

#### Problem Understanding:

- **Problem Explanation**: Determine if a 9x9 Sudoku board is valid. Each row, each column, and each of the nine 3x3 sub-boxes must contain the digits 1-9 without repetition. The board may be partially filled with empty cells represented by '.'.

**Example**:
Input:

```
[["5","3",".",".","7",".",".",".","."], 
 ["6",".",".","1","9","5",".",".","."], 
 [".","9","8",".",".",".",".","6","."], 
 ["8",".",".",".","6",".",".",".","3"], 
 ["4",".",".","8",".","3",".",".","1"], 
 ["7",".",".",".","2",".",".",".","6"], 
 [".","6",".",".",".",".","2","8","."], 
 [".",".",".","4","1","9",".",".","5"], 
 [".",".",".",".","8",".",".","7","9"]]
```

Output: `True`

#### Coding Pattern:

- The pattern here is **hashing**. We need to ensure there are no duplicate numbers in each row, column, and 3x3 grid. We can use sets to track the numbers we've seen in each of these regions.

#### Solution:

```python
def is_valid_sudoku(board):
    # Create sets to track the numbers seen in rows, columns, and boxes
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
  
    # Iterate over each cell in the 9x9 board
    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num == '.':
                continue  # Skip empty cells
          
            # Calculate the index for the 3x3 sub-box
            box_index = (i // 3) * 3 + (j // 3)
          
            # Check if the number is already seen in the current row, column, or box
            if num in rows[i] or num in cols[j] or num in boxes[box_index]:
                return False  # The board is invalid if there's a duplicate
          
            # Add the number to the respective row, column, and box sets
            rows[i].add(num)
            cols[j].add(num)
            boxes[box_index].add(num)
  
    return True  # If no duplicates were found, the board is valid

# Time Complexity: O(1) - since the board is always 9x9, the operations are constant
# Space Complexity: O(1) - the space for rows, cols, and boxes is fixed for a 9x9 board

# Test the function with the example
print(is_valid_sudoku([["5","3",".",".","7",".",".",".","."], 
                       ["6",".",".","1","9","5",".",".","."], 
                       [".","9","8",".",".",".",".","6","."], 
                       ["8",".",".",".","6",".",".",".","3"], 
                       ["4",".",".","8",".","3",".",".","1"], 
                       ["7",".",".",".","2",".",".",".","6"], 
                       [".","6",".",".",".",".","2","8","."], 
                       [".",".",".","4","1","9",".",".","5"], 
                       [".",".",".",".","8",".",".","7","9"]]))  
# Output: True
```

#### Alternative Approach:

- **No alternative approach** is required, as this is the optimal method for checking the validity of a Sudoku board.

---

### Problem 9: Longest Consecutive Sequence

#### Problem Understanding:

- **Problem Explanation**: You are given an unsorted array of integers. Find the length of the longest consecutive elements sequence. The solution must run in O(n) time.

**Example**:
Input: `[100, 4, 200, 1, 3, 2]`
Output: `4` (because the longest consecutive sequence is `[1, 2, 3, 4]`).

#### Coding Pattern:

- This problem can be solved using a **set**. By inserting all elements into a set and then checking for sequences starting with elements that do not have a smaller predecessor, we can efficiently find the longest consecutive sequence.

#### Solution:

```python
def longest_consecutive(nums):
    # Create a set to store all the unique numbers from the input array
    num_set = set(nums)
    longest_streak = 0  # Variable to track the longest consecutive sequence
  
    # Iterate through each number in the set
    for num in num_set:
        # Check if this number is the start of a new sequence (i.e., num-1 is not in the set)
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1  # Start a new streak
          
            # Continue the streak as long as the next consecutive number exists
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1  # Increment the streak length
          
            # Update the longest streak found so far
            longest_streak = max(longest_streak, current_streak)
  
    return longest_streak

# Time Complexity: O(n) - we traverse each element in the set once
# Space Complexity: O(n) - space for storing the set of numbers

# Test the function with the example
print(longest_consecutive([100, 4, 200, 1, 3, 2]))  # Output: 4
```

#### Alternative Approach:

- **No alternative approach** is needed because this approach provides the optimal O(n) time complexity solution.

---

## Two Pointers

### Problem 10: Valid Palindrome

#### Problem Understanding:

- **Problem Explanation**: Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases. For example, `"A man, a plan, a canal: Panama"` is a palindrome.

**Example**:
Input: `"A man, a plan, a canal: Panama"`
Output: `True`

#### Coding Pattern:

- This problem can be solved using the **Two Pointers** pattern. We use one pointer starting at the beginning and one at the end, skipping non-alphanumeric characters and comparing the remaining characters in a case-insensitive manner.

#### Solution:

```python
def is_palindrome(s):
    # Initialize two pointers, one at the start and one at the end of the string
    left, right = 0, len(s) - 1
  
    while left < right:
        # Move the left pointer to the next alphanumeric character
        while left < right and not s[left].isalnum():
            left += 1
      
        # Move the right pointer to the previous alphanumeric character
        while left < right and not s[right].isalnum():
            right -= 1
      
        # Compare the characters at left and right pointers (case-insensitive)
        if s[left].lower() != s[right].lower():
            return False  # Return False if the characters don't match
      
        # Move both pointers towards the center
        left += 1
        right -= 1
  
    return True  # Return True if all characters match

# Time Complexity: O(n) - we scan through the string once
# Space Complexity: O(1) - constant space used for the two pointers

# Test the function with the example
print(is_palindrome("A man, a plan, a canal: Panama"))  # Output: True
```

#### Alternative Approach:

- **No alternative approach** is needed because this two-pointer method efficiently solves the problem in O(n) time.

---

### Problem 11: Two Sum II - Input Array Is Sorted

#### Problem Understanding:

- **Problem Explanation**: Given an array of integers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target. You must return the indices of the two numbers (1-indexed).

**Example**:
Input: `numbers = [2, 7, 11, 15]`, `target = 9`
Output: `[1, 2]` (since 2 + 7 = 9)

#### Coding Pattern:

- Since the array is sorted, we can apply the **Two Pointers** technique. One pointer starts at the beginning and the other at the end. We check the sum of the two numbers, adjusting the pointers based on whether the sum is too small or too large.

#### Solution:

```python
def two_sum_sorted(numbers, target):
    # Initialize two pointers, one at the start and one at the end
    left, right = 0, len(numbers) - 1
  
    while left < right:
        current_sum = numbers[left] + numbers[right]  # Calculate the sum of the two pointers
      
        # If the sum matches the target, return the 1-indexed positions
        if current_sum == target:
            return [left + 1, right + 1]
      
        # If the sum is too small, move the left pointer to the right
        elif current_sum < target:
            left += 1
      
        # If the sum is too large, move the right pointer to the left
        else:
            right -= 1
  
    return []  # In case no solution exists

# Time Complexity: O(n) - we traverse the array once
# Space Complexity: O(1) - constant space used for the two pointers

# Test the function with the example
print(two_sum_sorted([2, 7, 11, 15], 9))  # Output: [1, 2]
```

#### Alternative Approach:

- **No alternative approach** is needed because the two-pointer approach is optimal for sorted arrays.

---

### Problem 12: 3Sum

#### Problem Understanding:

- **Problem Explanation**: Given an integer array `nums`, return all unique triplets that sum to zero. The solution set must not contain duplicate triplets.

**Example**:
Input: `[-1, 0, 1, 2, -1, -4]`
Output: `[[-1, -1, 2], [-1, 0, 1]]`

#### Coding Pattern:

- This problem is a variation of the **Two Pointers** technique but extended to three elements. First, sort the array, and then for each element, use two pointers to find pairs that sum to the negative of the current element.

#### Solution:

```python
def three_sum(nums):
    # Sort the array to use the two-pointer approach
    nums.sort()
    result = []
  
    # Iterate through the array, treating each number as the potential first element of a triplet
    for i in range(len(nums)):
        # Skip duplicate elements to avoid repeating triplets
        if i > 0 and nums[i] == nums[i - 1]:
            continue
      
        # Use two pointers to find two numbers that sum up to -nums[i]
        left, right = i + 1, len(nums) - 1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
          
            if current_sum == 0:
                result.append([nums[i], nums[left], nums[right]])
              
                # Move the left pointer and skip duplicates
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
              
                # Move the right pointer and skip duplicates
                right -= 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
          
            # If the sum is less than zero, move the left pointer to the right
            elif current_sum < 0:
                left += 1
          
            # If the sum is greater than zero, move the right pointer to the left
            else:
                right -= 1
  
    return result

# Time Complexity: O(n^2) - for each element, we perform a two-pointer search
# Space Complexity: O(1) - constant space used for the pointers (not counting the output list)

# Test the function with the example
print(three_sum([-1, 0, 1, 2, -1, -4]))  # Output: [[-1, -1, 2], [-1, 0, 1]]
```

#### Alternative Approach:

- **No alternative approach** is needed because this method, using sorting and two pointers, is the most efficient.

---

### Problem 13: Container With Most Water

#### Problem Understanding:

- **Problem Explanation**: Given `n` non-negative integers `a1, a2, ..., an`, where each represents a point at coordinate `(i, ai)`, the task is to find two lines that, together with the x-axis, form a container that holds the most water. The goal is to return the maximum amount of water the container can store.

**Example**:
Input: `[1,8,6,2,5,4,8,3,7]`
Output: `49` (between lines at indices 1 and 8, heights 8 and 7, area is 49).

#### Coding Pattern:

- This problem can be solved using the **Two Pointers** technique. We initialize two pointers, one at the beginning and the other at the end, and calculate the area. Then, we move the pointer that points to the shorter line inward, aiming to maximize the area.

#### Solution:

```python
def max_area(height):
    # Initialize two pointers at the beginning and end of the list
    left, right = 0, len(height) - 1
    max_water = 0  # Variable to store the maximum amount of water
  
    # Continue moving the pointers towards each other
    while left < right:
        # Calculate the current area (distance between pointers * height of shorter line)
        current_area = (right - left) * min(height[left], height[right])
      
        # Update the maximum water if the current area is larger
        max_water = max(max_water, current_area)
      
        # Move the pointer that points to the shorter line
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
  
    return max_water

# Time Complexity: O(n) - we traverse the list once with two pointers
# Space Complexity: O(1) - constant space used for the two pointers

# Test the function with the example
print(max_area([1,8,6,2,5,4,8,3,7]))  # Output: 49
```

#### Alternative Approach:

- **No alternative approach** is needed as the two-pointer technique provides an efficient solution in O(n) time.

---

### Problem 14: Trapping Rain Water

#### Problem Understanding:

- **Problem Explanation**: Given `n` non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

**Example**:
Input: `[0,1,0,2,1,0,1,3,2,1,2,1]`
Output: `6` (The trapped water is above the bars at indices 2, 4, 5, 6, 9).

#### Coding Pattern:

- This problem can be solved using the **Two Pointers** pattern, where we maintain two pointers and track the maximum heights on the left and right of the current position. We calculate how much water can be trapped at each step.

#### Solution:

```python
def trap(height):
    # Initialize two pointers, one at the start and one at the end of the list
    left, right = 0, len(height) - 1
    left_max, right_max = 0, 0  # Variables to track the maximum heights on the left and right
    water_trapped = 0  # Variable to store the total amount of trapped water
  
    # Continue processing while the two pointers don't cross
    while left < right:
        # If the left height is smaller, process from the left side
        if height[left] < height[right]:
            # Update the maximum height on the left
            if height[left] >= left_max:
                left_max = height[left]
            else:
                # Calculate trapped water based on the difference between the max height and current height
                water_trapped += left_max - height[left]
            left += 1
        # If the right height is smaller, process from the right side
        else:
            # Update the maximum height on the right
            if height[right] >= right_max:
                right_max = height[right]
            else:
                # Calculate trapped water based on the difference between the max height and current height
                water_trapped += right_max - height[right]
            right -= 1
  
    return water_trapped

# Time Complexity: O(n) - we traverse the list once with two pointers
# Space Complexity: O(1) - constant space used for the two pointers

# Test the function with the example
print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))  # Output: 6
```

#### Alternative Approach:

- **No alternative approach** is needed, as this two-pointer solution is optimal for this problem, achieving O(n) time complexity.

---

## Sliding Window

### Problem 15: Best Time to Buy and Sell Stock

#### Problem Understanding:

- **Problem Explanation**: You are given an array where each element represents the price of a given stock on that day. You want to maximize your profit by choosing a single day to buy one stock and another day in the future to sell it. Find the maximum profit you can achieve.

**Example**:
Input: `[7,1,5,3,6,4]`
Output: `5` (buy on day 2 at price 1 and sell on day 5 at price 6, profit = 6 - 1 = 5).

#### Coding Pattern:

- This problem can be solved using a **Single Pass** approach. We iterate through the array, keeping track of the minimum price seen so far and calculating the maximum profit we can get if we sell on each day.

#### Solution:

```python
def max_profit(prices):
    # Initialize variables to track the minimum price and the maximum profit
    min_price = float('inf')
    max_profit = 0
  
    # Iterate through the list of prices
    for price in prices:
        # Update the minimum price if we find a new lower price
        if price < min_price:
            min_price = price
        # Calculate the profit if we sell at the current price
        elif price - min_price > max_profit:
            max_profit = price - min_price
  
    return max_profit

# Time Complexity: O(n) - we traverse the list once
# Space Complexity: O(1) - constant space used for tracking the minimum price and maximum profit

# Test the function with the example
print(max_profit([7,1,5,3,6,4]))  # Output: 5
```

#### Alternative Approach:

- **No alternative approach** is needed, as this single-pass solution provides the optimal result in O(n) time.

---

### Problem 16: Longest Substring Without Repeating Characters

#### Problem Understanding:

- **Problem Explanation**: Given a string `s`, find the length of the longest substring without repeating characters.

**Example**:
Input: `"abcabcbb"`
Output: `3` (The answer is `"abc"`, with the length of 3).

#### Coding Pattern:

- This problem can be solved using the **Sliding Window** pattern. We use a sliding window to keep track of the current substring without repeating characters, adjusting the window as needed.

#### Solution:

```python
def length_of_longest_substring(s):
    # Dictionary to store the last index of each character
    char_map = {}
    left = 0  # Left boundary of the sliding window
    max_length = 0  # Variable to store the maximum length of the substring
  
    # Iterate through the string with the right boundary of the window
    for right in range(len(s)):
        # If the character is already in the window, move the left boundary
        if s[right] in char_map and char_map[s[right]] >= left:
            left = char_map[s[right]] + 1
      
        # Update the last seen index of the character
        char_map[s[right]] = right
      
        # Update the maximum length of the substring
        max_length = max(max_length, right - left + 1)
  
    return max_length

# Time Complexity: O(n) - we traverse the string once with the sliding window
# Space Complexity: O(min(n, m)) - where n is the length of the string, and m is the character set (26 for lowercase letters)

# Test the function with the example
print(length_of_longest_substring("abcabcbb"))  # Output: 3
```

#### Alternative Approach:

- **No alternative approach** is needed, as this sliding window solution provides an optimal O(n) time complexity result.

---

### Problem 17: Longest Repeating Character Replacement

#### Problem Understanding:

- **Problem Explanation**: Given a string `s` and an integer `k`, you can replace any character in the string with another character `k` times. The goal is to find the length of the longest substring containing the same letter after performing the replacements.

**Example**:
Input: `s = "AABABBA", k = 1`
Output: `4` (After replacing one 'B', the substring `"AABA"` becomes the longest).

#### Coding Pattern:

- This problem can be solved using the **Sliding Window** pattern. The idea is to expand the window to include more characters, but shrink it when the condition (allowing at most `k` replacements) is violated.

#### Solution:

```python
def character_replacement(s, k):
    # Dictionary to count the frequency of characters in the current window
    count = {}
    left = 0  # Left boundary of the sliding window
    max_count = 0  # To track the count of the most frequent character in the window
    max_length = 0  # Variable to store the maximum length of the valid substring
  
    # Iterate through the string with the right boundary of the window
    for right in range(len(s)):
        count[s[right]] = count.get(s[right], 0) + 1  # Increment the count of the current character
      
        # Update the max_count with the most frequent character's count
        max_count = max(max_count, count[s[right]])
      
        # If the window size minus the most frequent character's count is greater than k, shrink the window
        if right - left + 1 - max_count > k:
            count[s[left]] -= 1  # Decrement the count of the left character
            left += 1  # Shrink the window by moving the left pointer to the right
      
        # Calculate the maximum length of the valid substring
        max_length = max(max_length, right - left + 1)
  
    return max_length

# Time Complexity: O(n) - we traverse the string once with the sliding window
# Space Complexity: O(1) - since the character count dictionary has at most 26 entries (for uppercase letters)

# Test the function with the example
print(character_replacement("AABABBA", 1))  # Output: 4
```

#### Alternative Approach:

- **No alternative approach** is necessary, as the sliding window approach provides the optimal O(n) solution.

---

### Problem 18: Permutation in String

#### Problem Understanding:

- **Problem Explanation**: Given two strings `s1` and `s2`, return `True` if `s2` contains a permutation of `s1`. In other words, check if one of `s1`'s permutations is a substring of `s2`.

**Example**:
Input: `s1 = "ab"`, `s2 = "eidbaooo"`
Output: `True` (because `"ba"` is a permutation of `"ab"` and is a substring of `s2`).

#### Coding Pattern:

- This problem can be solved using the **Sliding Window** pattern combined with **Hashing**. We use a sliding window of size equal to `s1` and check whether the character counts in the window match those in `s1`.

#### Solution:

```python
def check_inclusion(s1, s2):
    # Edge case: if s1 is longer than s2, s2 cannot contain its permutation
    if len(s1) > len(s2):
        return False
  
    # Arrays to store the character counts of s1 and the current window in s2
    s1_count = [0] * 26
    s2_count = [0] * 26
  
    # Count the frequency of characters in s1
    for char in s1:
        s1_count[ord(char) - ord('a')] += 1
  
    # Use a sliding window to compare character counts in s2
    for i in range(len(s2)):
        # Add the current character in the window
        s2_count[ord(s2[i]) - ord('a')] += 1
      
        # Remove the character that's sliding out of the window
        if i >= len(s1):
            s2_count[ord(s2[i - len(s1)]) - ord('a')] -= 1
      
        # If the character counts in the window match those in s1, return True
        if s1_count == s2_count:
            return True
  
    return False

# Time Complexity: O(n) - where n is the length of s2 (sliding window of size len(s1))
# Space Complexity: O(1) - fixed space for the character count arrays (26 for lowercase letters)

# Test the function with the example
print(check_inclusion("ab", "eidbaooo"))  # Output: True
```

#### Alternative Approach:

- **No alternative approach** is required, as the sliding window approach with character counts is optimal.

---

### Problem 19: Minimum Window Substring

#### Problem Understanding:

- **Problem Explanation**: Given two strings `s` and `t`, return the minimum window in `s` which contains all the characters in `t`. If there is no such window, return an empty string.

**Example**:
Input: `s = "ADOBECODEBANC"`, `t = "ABC"`
Output: `"BANC"` (because this is the smallest window that contains all characters from `t`).

#### Coding Pattern:

- This problem can be solved using the **Sliding Window** pattern. The goal is to expand the window until all characters in `t` are included, and then contract the window to find the smallest possible substring.

#### Solution:

```python
def min_window(s, t):
    if not t or not s:
        return ""
  
    # Dictionary to count the frequency of characters in t
    dict_t = {}
    for char in t:
        dict_t[char] = dict_t.get(char, 0) + 1
  
    required = len(dict_t)  # Number of unique characters in t
    left, right = 0, 0  # Pointers for the sliding window
    formed = 0  # To track how many unique characters in t are satisfied in the window
  
    # Dictionary to count the characters in the current window
    window_counts = {}
    # (window length, left, right) to store the smallest window found
    ans = float("inf"), None, None
  
    # Start expanding the window
    while right < len(s):
        char = s[right]
        window_counts[char] = window_counts.get(char, 0) + 1
      
        # If the current character's frequency in the window matches t's, update formed
        if char in dict_t and window_counts[char] == dict_t[char]:
            formed += 1
      
        # Try to contract the window until it's no longer valid
        while left <= right and formed == required:
            char = s[left]
          
            # Update the result if this window is smaller than the previous smallest
            if right - left + 1 < ans[0]:
                ans = (right - left + 1, left, right)
          
            # Remove the leftmost character and shrink the window
            window_counts[char] -= 1
            if char in dict_t and window_counts[char] < dict_t[char]:
                formed -= 1
          
            left += 1  # Move the left pointer to shrink the window
      
        # Expand the window by moving the right pointer
        right += 1
  
    # If no valid window was found, return an empty string
    return "" if ans[1] is None else s[ans[1]:ans[2] + 1]

# Time Complexity: O(n + m) - where n is the length of s and m is the length of t
# Space Complexity: O(n + m) - for the dictionaries used to store counts of s and t

# Test the function with the example
print(min_window("ADOBECODEBANC", "ABC"))  # Output: "BANC"
```

#### Alternative Approach:

- **No alternative approach** is needed, as the sliding window with dictionary counting is efficient for this problem.

---

### Problem 20: Sliding Window Maximum

#### Problem Understanding:

- **Problem Explanation**: Given an array `nums` and an integer `k`, you need to find the maximum value in every sliding window of size `k` in the array.

**Example**:
Input: `nums = [1,3,-1,-3,5,3,6,7]`, `k = 3`
Output: `[3,3,5,5,6,7]`

#### Coding Pattern:

- This problem can be solved using a **Deque** (double-ended queue). The idea is to maintain a deque where the front holds the index of the maximum element in the current window, and we adjust it as the window slides.

#### Solution:

```python
from collections import deque

def max_sliding_window(nums, k):
    # Deque to store indices of potential maximum elements
    dq = deque()
    result = []
  
    # Iterate through each element in the array
    for i in range(len(nums)):
        # Remove elements that are outside the current window
        if dq and dq[0] < i - k + 1:
            dq.popleft()
      
        # Remove elements that are smaller than

 the current element (since they can't be the max)
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
      
        # Add the current element's index to the deque
        dq.append(i)
      
        # If the window is fully within the array, add the maximum to the result
        if i >= k - 1:
            result.append(nums[dq[0]])  # The front of the deque is the maximum element in the window
  
    return result

# Time Complexity: O(n) - each element is added and removed from the deque at most once
# Space Complexity: O(k) - for storing the indices in the deque

# Test the function with the example
print(max_sliding_window([1,3,-1,-3,5,3,6,7], 3))  # Output: [3, 3, 5, 5, 6, 7]
```

#### Alternative Approach:

- **No alternative approach** is needed, as using a deque provides the optimal O(n) solution.

---

## Stack

### Problem 21: Valid Parentheses

#### Problem Understanding:

- **Problem Explanation**: Given a string containing just the characters `'('`, `')'`, `'{', '}', '[', ']'`, determine if the input string is valid. A valid string must have matching open and close parentheses, and they must be in the correct order.

**Example**:
Input: `"()[]{}"`
Output: `True`

#### Coding Pattern:

- This problem is solved using the **Stack** pattern. We push open parentheses onto a stack, and for every closing parenthesis, we check if the top of the stack contains the corresponding open parenthesis.

#### Solution:

```python
def is_valid(s):
    # Stack to store open brackets
    stack = []
  
    # Dictionary to store matching pairs of parentheses
    mapping = {')': '(', '}': '{', ']': '['}
  
    # Iterate over the characters in the input string
    for char in s:
        # If the character is a closing parenthesis
        if char in mapping:
            # Pop the top of the stack (if stack is empty, use a dummy value '#')
            top_element = stack.pop() if stack else '#'
          
            # Check if the popped element is the corresponding open parenthesis
            if mapping[char] != top_element:
                return False
        else:
            # If it's an opening parenthesis, push it onto the stack
            stack.append(char)
  
    # The string is valid if the stack is empty at the end (all parentheses matched)
    return not stack

# Time Complexity: O(n) - where n is the length of the string
# Space Complexity: O(n) - for the stack that stores open parentheses

# Test the function with the example
print(is_valid("()[]{}"))  # Output: True
```

#### Alternative Approach:

- **No alternative approach** is required as the stack-based solution efficiently solves the problem in O(n) time.

---

### Problem 22: Min Stack

#### Problem Understanding:

- **Problem Explanation**: Design a stack that supports push, pop, top, and retrieving the minimum element in constant time. Implement `MinStack` with these methods:
  - `push(val)`: Pushes `val` onto the stack.
  - `pop()`: Removes the element on the top of the stack.
  - `top()`: Gets the top element.
  - `get_min()`: Retrieves the minimum element in the stack.

**Example**:
Input:

```
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.get_min(); // Returns -3
minStack.pop();
minStack.top();      // Returns 0
minStack.get_min();  // Returns -2
```

#### Coding Pattern:

- We can solve this by maintaining two stacks: one for all elements and another for tracking the minimum elements.

#### Solution:

```python
class MinStack:
    def __init__(self):
        # Initialize two stacks: one for all elements and one for the minimum elements
        self.stack = []
        self.min_stack = []

    def push(self, val: int):
        # Push the value onto the main stack
        self.stack.append(val)
        # If the min_stack is empty or the current value is smaller or equal to the top of the min_stack, push it
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        # Pop the value from the main stack
        if self.stack:
            val = self.stack.pop()
            # If the popped value is the same as the top of the min_stack, pop it from the min_stack as well
            if val == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self):
        # Return the top element of the stack
        return self.stack[-1] if self.stack else None

    def get_min(self):
        # Return the top element of the min_stack (the minimum element in the stack)
        return self.min_stack[-1] if self.min_stack else None

# Time Complexity for all operations: O(1) - constant time for push, pop, top, and get_min
# Space Complexity: O(n) - where n is the number of elements in the stack

# Test the MinStack class
min_stack = MinStack()
min_stack.push(-2)
min_stack.push(0)
min_stack.push(-3)
print(min_stack.get_min())  # Output: -3
min_stack.pop()
print(min_stack.top())      # Output: 0
print(min_stack.get_min())  # Output: -2
```

#### Alternative Approach:

- **No alternative approach** is necessary, as this solution already provides constant time complexity for all operations.

---

### Problem 23: Evaluate Reverse Polish Notation

#### Problem Understanding:

- **Problem Explanation**: Evaluate the value of an arithmetic expression in Reverse Polish Notation (RPN). Valid operators are `+`, `-`, `*`, and `/`. Each operand may be an integer, and division should truncate towards zero.

**Example**:
Input: `["2", "1", "+", "3", "*"]`
Output: `9`
Explanation: `((2 + 1) * 3) = 9`

#### Coding Pattern:

- This problem can be solved using the **Stack** pattern. We push operands onto the stack, and when encountering an operator, we pop two elements, perform the operation, and push the result back onto the stack.

#### Solution:

```python
def eval_rpn(tokens):
    # Stack to store the operands
    stack = []
  
    # Iterate through each token
    for token in tokens:
        # If the token is an operator, pop two elements, perform the operation, and push the result
        if token in "+-*/":
            b = stack.pop()  # Second operand
            a = stack.pop()  # First operand
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                # Integer division (truncating towards zero)
                stack.append(int(a / b))
        else:
            # If the token is a number, push it onto the stack
            stack.append(int(token))
  
    # The final result will be the only element left in the stack
    return stack.pop()

# Time Complexity: O(n) - where n is the number of tokens in the input
# Space Complexity: O(n) - for the stack used to store operands

# Test the function with the example
print(eval_rpn(["2", "1", "+", "3", "*"]))  # Output: 9
```

#### Alternative Approach:

- **No alternative approach** is required because the stack-based solution is efficient for this problem, and there are no faster approaches.

---

### Problem 24: Generate Parentheses

#### Problem Understanding:

- **Problem Explanation**: Given `n` pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

**Example**:
Input: `n = 3`
Output:

```
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
```

#### Coding Pattern:

- This problem can be solved using **Backtracking**. We recursively generate strings by adding open and close parentheses, ensuring that we always add valid parentheses combinations.

#### Solution:

```python
def generate_parenthesis(n):
    def backtrack(s, left, right):
        # If the current string is of length 2*n, it's a valid combination
        if len(s) == 2 * n:
            result.append(s)
            return
      
        # If we can still add an open parenthesis, do so
        if left < n:
            backtrack(s + '(', left + 1, right)
      
        # If we can still add a close parenthesis, do so
        if right < left:
            backtrack(s + ')', left, right + 1)
  
    result = []
    backtrack("", 0, 0)
    return result

# Time Complexity: O(4^n / sqrt(n)) - the number of valid parentheses combinations is a Catalan number
# Space Complexity: O(4^n / sqrt(n)) - for storing the valid combinations

# Test the function with the example
print(generate_parenthesis(3))
# Output: ['((()))', '(()())', '(())()', '()(())', '()()()']
```

#### Alternative Approach:

- **No alternative approach** is required, as this backtracking solution is optimal for generating all valid combinations.

---

### Problem 25: Daily Temperatures

#### Problem Understanding:

- **Problem Explanation**: Given an array of daily temperatures `T`, return an array `answer` such that `answer[i]` is the number of days you would have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, put `0` instead.

**Example**:
Input: `T = [73, 74, 75, 71, 69, 72, 76, 73]`
Output: `[1, 1, 4, 2, 1, 1, 0, 0]`

#### Coding Pattern:

- The problem can be efficiently solved using a **Monotonic Stack**. The idea is to store indices of days in a stack such that the temperatures are in decreasing order. Whenever a warmer day is found, we pop from the stack and calculate the difference in indices.

#### Solution:

```python
def daily_temperatures(T):
    # Stack to store the indices of days
    stack = []
    # Initialize the answer array with all zeros
    answer = [0] * len(T)
  
    # Iterate through the temperature list
    for i, temp in enumerate(T):
        # Check if the current temperature is warmer than the temperatures at the indices in the stack
        while stack and T[stack[-1]] < temp:
            prev_day = stack.pop()
            answer[prev_day] = i - prev_day  # Calculate the number of days to wait for a warmer temperature
      
        # Push the current index onto the stack
        stack.append(i)
  
    return answer

# Time Complexity: O(n) - we process each element at most twice (push and pop from the stack)
# Space Complexity: O(n) - for the stack storing indices

# Test the function with the example
print(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))  # Output: [1, 1, 4, 2, 1, 1, 0, 0]
```

#### Alternative Approach:

- **No alternative approach** is required, as the monotonic stack solution is optimal.

---

### Problem 26: Car Fleet

#### Problem Understanding:

- **Problem Explanation**: There are `n` cars going to the same destination along a one-lane road. The destination is `target` miles away. Each car `i` has a position `position[i]` and speed `speed[i]`. A car can never pass another car, but it can catch up to it, forming a fleet. The goal is to return the number of car fleets that will arrive at the destination.

**Example**:
Input: `target = 12`, `position = [10, 8, 0, 5, 3]`, `speed = [2, 4, 1, 1, 3]`
Output: `3` (Cars form 3 different fleets).

#### Coding Pattern:

- The problem can be solved using sorting and a **Greedy** approach. We sort the cars by their starting positions (from farthest to closest) and calculate how long it will take each car to reach the destination. Cars that catch up to others form a fleet.

#### Solution:

```python
def car_fleet(target, position, speed):
    # Create pairs of (position, time to reach the target)
    cars = [(p, (target - p) / s) for p, s in zip(position, speed)]
  
    # Sort the cars by their starting positions in descending order
    cars.sort(reverse=True)
  
    fleets = 0  # Number of car fleets
    current_fleet_time = 0  # Time taken by the leading car in the current fleet
  
    # Iterate through the sorted cars
    for pos, time in cars:
        # If the current car cannot catch up with the fleet in front, it forms a new fleet
        if time > current_fleet_time:
            fleets += 1
            current_fleet_time = time  # Update the fleet time with the current car's time
  
    return fleets

# Time Complexity: O(n log n) - sorting the cars by position
# Space Complexity: O(n) - for storing the position and time pairs

# Test the function with the example
print(car_fleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))  # Output: 3
```

#### Alternative Approach:

- **No alternative approach** is needed as the sorting and greedy approach provides an optimal solution.

---

### Problem 27: Largest Rectangle in Histogram

#### Problem Understanding:

- **Problem Explanation**: Given an array of integers representing the heights of bars in a histogram, return the area of the largest rectangle that can be formed within the bounds of the histogram.

**Example**:
Input: `heights = [2, 1, 5, 6, 2, 3]`
Output: `10` (The largest rectangle has height 5 and width 2, area = 5 * 2 = 10).

#### Coding Pattern:

- This problem can be efficiently solved using a **Monotonic Stack**. The stack helps to keep track of indices of bars in increasing order of height, and we calculate the area whenever we find a bar shorter than the top of the stack.

#### Solution:

```python
def largest_rectangle_area(heights):
    # Initialize the stack and the maximum area variable
    stack = []
    max_area = 0
  
    # Append a zero height to handle remaining bars in the stack at the end
    heights.append(0)
  
    # Iterate through the heights
    for i, h in enumerate(heights):
        # While the current height is less than the height of the bar at the top of the stack
        while stack and heights[stack[-1]] > h:
            # Pop the top of the stack and calculate the area with the popped height
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1  # Calculate the width of the rectangle
            max_area = max(max_area, height * width)  # Update the maximum area
      
        # Push the current index onto the stack
        stack.append(i)
  
    # Return the maximum area found
    return max_area

# Time Complexity: O(n) - we traverse the heights array and process each element at most twice
# Space Complexity: O(n) - for the stack used to store indices

# Test the function with the example
print(largest_rectangle_area([2, 1, 5, 6, 2, 3]))  # Output: 10
```

#### Alternative Approach:

- **No alternative approach** is needed as the monotonic stack provides an optimal solution in O(n) time.

## Binary Search Section

### Problem 1: Binary Search

#### Problem Understanding:

- **Problem Explanation**: Given a sorted array of integers, write a function to search for a target value. If the target exists, return its index. If not, return `-1`.

**Example**:
Input: `nums = [-1, 0, 3, 5, 9, 12]`, `target = 9`
Output: `4` (target is at index 4).

#### Coding Pattern:

- This problem can be solved using **Binary Search** since the array is sorted.

#### Solution:

```python
def binary_search(nums, target):
    left, right = 0, len(nums) - 1
  
    # Perform binary search
    while left <= right:
        mid = left + (right - left) // 2  # Calculate the middle index
      
        # If target is found, return the index
        if nums[mid] == target:
            return mid
      
        # If target is smaller than the middle element, search in the left half
        elif nums[mid] > target:
            right = mid - 1
      
        # If target is larger, search in the right half
        else:
            left = mid + 1
  
    return -1  # Target not found

# Time Complexity: O(log n) - binary search divides the array in half each time
# Space Complexity: O(1) - only a few variables are used for searching

# Test the function with the example
print(binary_search([-1, 0, 3, 5, 9, 12], 9))  # Output: 4
```

#### Alternative Approach:

- **No alternative approach** is required, as binary search is the most optimal solution for this problem.

---

### Problem 2: Search a 2D Matrix

#### Problem Understanding:

- **Problem Explanation**: Write an efficient algorithm that searches for a target value in an `m x n` matrix. The matrix has the following properties:
  1. Each row is sorted in ascending order.
  2. The first integer of each row is greater than the last integer of the previous row.

**Example**:
Input: `matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]`, `target = 3`
Output: `True` (target is found).

#### Coding Pattern:

- This problem can be solved by treating the 2D matrix as a flattened sorted array and using **Binary Search**.

#### Solution:

```python
def search_matrix(matrix, target):
    # If the matrix is empty, return False
    if not matrix or not matrix[0]:
        return False
  
    m, n = len(matrix), len(matrix[0])  # Dimensions of the matrix
    left, right = 0, m * n - 1  # Treat the matrix as a flat array
  
    # Perform binary search
    while left <= right:
        mid = left + (right - left) // 2
        mid_value = matrix[mid // n][mid % n]  # Convert 1D index to 2D index
      
        # If target is found, return True
        if mid_value == target:
            return True
      
        # If target is smaller, search the left half
        elif mid_value > target:
            right = mid - 1
      
        # If target is larger, search the right half
        else:
            left = mid + 1
  
    return False  # Target not found

# Time Complexity: O(log(m * n)) - binary search in a matrix of m rows and n columns
# Space Complexity: O(1) - only a few variables are used for searching

# Test the function with the example
print(search_matrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))  # Output: True
```

#### Alternative Approach:

- **No alternative approach** is required, as binary search is optimal.

---

### Problem 3: Koko Eating Bananas

#### Problem Understanding:

- **Problem Explanation**: Koko loves to eat bananas. There are `n` piles of bananas, the ith pile has `piles[i]` bananas. Koko wants to finish eating all the bananas in `h` hours. She can decide her banana eating speed `k`, which is the number of bananas per hour. Find the minimum integer `k` such that she can finish all the bananas within `h` hours.

**Example**:
Input: `piles = [3, 6, 7, 11]`, `h = 8`
Output: `4` (minimum speed is 4 bananas/hour).

#### Coding Pattern:

- This problem can be solved using **Binary Search** on the potential values of `k`.

#### Solution:

```python
import math

def min_eating_speed(piles, h):
    # Define the range of possible speeds (from 1 to max of piles)
    left, right = 1, max(piles)
  
    # Perform binary search to find the minimum speed
    while left < right:
        mid = (left + right) // 2
        hours_needed = sum(math.ceil(pile / mid) for pile in piles)
      
        # If she can finish in the given time, search for a smaller speed
        if hours_needed <= h:
            right = mid
        else:
            left = mid + 1
  
    return left

# Time Complexity: O(n log max(piles)) - binary search on speed, and for each speed, sum over piles
# Space Complexity: O(1) - only a few variables are used for searching

# Test the function with the example
print(min_eating_speed([3, 6, 7, 11], 8))  # Output: 4
```

#### Alternative Approach:

- **No alternative approach** is required, as binary search on the speed is optimal.

---

### Problem 4: Find Minimum in Rotated Sorted Array

#### Problem Understanding:

- **Problem Explanation**: Suppose an array of sorted integers is rotated at some pivot. You need to find the minimum element in the array without any duplicates.

**Example**:
Input: `nums = [3, 4, 5, 1, 2]`
Output: `1`

#### Coding Pattern:

- This problem can be solved using **Binary Search** in a rotated array.

#### Solution:

```python
def find_min(nums):
    left, right = 0, len(nums) - 1
  
    # Perform binary search to find the minimum element
    while left < right:
        mid = left + (right - left) // 2
      
        # If mid is greater than right, the minimum is in the right half
        if nums[mid] > nums[right]:
            left = mid + 1
        # Otherwise, it's in the left half (including mid)
        else:
            right = mid
  
    return nums[left]

# Time Complexity: O(log n) - binary search in the rotated sorted array
# Space Complexity: O(1) - constant space is used

# Test the function with the example
print(find_min([3, 4, 5, 1, 2]))  # Output: 1
```

#### Alternative Approach:

- **No alternative approach** is required, as binary search is optimal for finding the minimum in a rotated sorted array.

---

### Problem 5: Search in Rotated Sorted Array

#### Problem Understanding:

- **Problem Explanation**: You are given a rotated sorted array, and you need to search for a target value. If found, return its index, otherwise return `-1`.

**Example**:
Input: `nums = [4, 5, 6, 7, 0, 1, 2]`, `target = 0`
Output: `4`

#### Coding Pattern:

- This problem can be solved using **Binary Search** in a rotated sorted array.

#### Solution:

```python
def search(nums, target):
    left, right = 0, len(nums) - 1
  
    # Perform binary search
    while left <= right:
        mid = left + (right - left) // 2
      
        # If target is found, return the index
        if nums[mid] == target:
            return mid
      
        # If the left half is sorted
        if nums[left] <= nums[mid]:
            # Check if the target lies within the left half
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # If the right half is sorted
        else:
            # Check if the target lies within the right half
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
  
    return -1

# Time Complexity: O(log n) - binary search in the rotated sorted array
# Space Complexity: O(1) - constant space is used

# Test the function with the example
print(search([4, 5, 6, 7, 0, 1, 2], 0))  # Output: 4


```

#### Alternative Approach:

- **No alternative approach** is needed, as binary search is optimal.

---

### Problem 6: Time Based Key-Value Store

#### Problem Understanding:

- **Problem Explanation**: Design a time-based key-value store that supports two operations:
  - `set(key, value, timestamp)`: Stores the key and value, along with the given timestamp.
  - `get(key, timestamp)`: Returns the value associated with the key at the largest timestamp `≤ timestamp`. If there is no such timestamp, return an empty string `""`.

**Example**:

```
Input:
timeMap.set("foo", "bar", 1);
timeMap.get("foo", 1); // returns "bar"
timeMap.get("foo", 3); // returns "bar"
timeMap.set("foo", "bar2", 4);
timeMap.get("foo", 4); // returns "bar2"
timeMap.get("foo", 5); // returns "bar2"
```

#### Coding Pattern:

- We can solve this problem using **Binary Search** over the timestamps for each key. A dictionary will store each key and a list of `(timestamp, value)` pairs, and binary search will be used to find the appropriate value for a given timestamp.

#### Solution:

```python
from collections import defaultdict
import bisect

class TimeMap:
    def __init__(self):
        # Dictionary to store key as the key and a list of (timestamp, value) pairs as the value
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Append the (timestamp, value) pair to the list for the key
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # Use binary search to find the largest timestamp ≤ the given timestamp
        values = self.store.get(key, [])
        i = bisect.bisect_right(values, (timestamp, chr(127)))  # `chr(127)` ensures it's the largest possible character
        return values[i - 1][1] if i > 0 else ""

# Time Complexity: 
# - set: O(1) to append a value.
# - get: O(log n) to binary search for the timestamp in the list.
# Space Complexity: O(n) - where n is the number of set operations.

# Test the class with the example
timeMap = TimeMap()
timeMap.set("foo", "bar", 1)
print(timeMap.get("foo", 1))  # Output: "bar"
print(timeMap.get("foo", 3))  # Output: "bar"
timeMap.set("foo", "bar2", 4)
print(timeMap.get("foo", 4))  # Output: "bar2"
print(timeMap.get("foo", 5))  # Output: "bar2"
```

#### Alternative Approach:

- **No alternative approach** is needed as binary search efficiently solves this problem in O(log n) time for each query.

---

### Problem 7: Median of Two Sorted Arrays

#### Problem Understanding:

- **Problem Explanation**: Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return the median of the two sorted arrays.

**Example**:
Input: `nums1 = [1, 3]`, `nums2 = [2]`
Output: `2.0` (merged array is [1, 2, 3] and the median is 2).

#### Coding Pattern:

- This problem can be solved using **Binary Search** on the smaller array. The goal is to partition both arrays such that the left half of the merged array contains all smaller elements, and the right half contains all larger elements.

#### Solution:

```python
def find_median_sorted_arrays(nums1, nums2):
    # Ensure nums1 is the smaller array for binary search
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
  
    m, n = len(nums1), len(nums2)
    half_len = (m + n + 1) // 2
  
    # Perform binary search on the smaller array
    left, right = 0, m
    while left <= right:
        i = (left + right) // 2
        j = half_len - i
      
        # Check if i is too small (nums1[i] < nums2[j-1])
        if i < m and nums2[j-1] > nums1[i]:
            left = i + 1
        # Check if i is too large (nums1[i-1] > nums2[j])
        elif i > 0 and nums1[i-1] > nums2[j]:
            right = i - 1
        else:
            # Find the maximum of the left partition
            if i == 0: max_of_left = nums2[j-1]
            elif j == 0: max_of_left = nums1[i-1]
            else: max_of_left = max(nums1[i-1], nums2[j-1])
          
            # If the total number of elements is odd, return max_of_left
            if (m + n) % 2 == 1:
                return max_of_left
          
            # Find the minimum of the right partition
            if i == m: min_of_right = nums2[j]
            elif j == n: min_of_right = nums1[i]
            else: min_of_right = min(nums1[i], nums2[j])
          
            # Return the average of the two middle elements
            return (max_of_left + min_of_right) / 2

# Time Complexity: O(log(min(m, n))) - binary search on the smaller array
# Space Complexity: O(1) - constant space used

# Test the function with the example
print(find_median_sorted_arrays([1, 3], [2]))  # Output: 2.0
```

#### Alternative Approach:

- **No alternative approach** is needed, as binary search on the smaller array is optimal.

---

## Linked List Section

### Problem 8: Reverse Linked List

#### Problem Understanding:

- **Problem Explanation**: Given the head of a singly linked list, reverse the list and return the reversed list.

**Example**:
Input: `head = [1, 2, 3, 4, 5]`
Output: `[5, 4, 3, 2, 1]`

#### Coding Pattern:

- This problem can be solved using **Iterative** or **Recursive** approaches. We'll first solve it iteratively by reversing the pointers between nodes.

#### Solution (Iterative):

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head):
    prev = None  # Initialize prev to None to mark the end of the reversed list
    current = head
  
    # Traverse the list and reverse the pointers
    while current:
        next_node = current.next  # Save the next node
        current.next = prev  # Reverse the pointer
        prev = current  # Move prev to current
        current = next_node  # Move to the next node
  
    return prev  # prev will be the new head of the reversed list

# Time Complexity: O(n) - where n is the number of nodes in the list
# Space Complexity: O(1) - constant space used for pointer manipulation

# Test the function (you can write test cases with a linked list structure)
```

#### Alternative Approach (Recursive):

```python
def reverse_list_recursive(head):
    # Base case: if head is empty or only one node, return it
    if not head or not head.next:
        return head
  
    # Reverse the rest of the list recursively
    new_head = reverse_list_recursive(head.next)
  
    # Adjust the pointers to reverse the current pair of nodes
    head.next.next = head
    head.next = None
  
    return new_head

# Time Complexity: O(n) - where n is the number of nodes in the list
# Space Complexity: O(n) - due to the recursion stack
```

---

### Problem 9: Merge Two Sorted Lists

#### Problem Understanding:

- **Problem Explanation**: Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

**Example**:
Input: `l1 = [1, 2, 4]`, `l2 = [1, 3, 4]`
Output: `[1, 1, 2, 3, 4, 4]`

#### Coding Pattern:

- This problem can be solved using **Two Pointers**. We can traverse both lists and merge them into one by comparing node values.

#### Solution:

```python
def merge_two_lists(l1, l2):
    # Create a dummy node to serve as the head of the merged list
    dummy = ListNode()
    current = dummy
  
    # Traverse both lists and merge them
    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
  
    # Attach the remaining elements, if any
    if

 l1:
        current.next = l1
    else:
        current.next = l2
  
    return dummy.next

# Time Complexity: O(n + m) - where n and m are the lengths of the two lists
# Space Complexity: O(1) - constant space (apart from the input list space)

# Test the function with example linked lists
```

#### Alternative Approach:

- **No alternative approach** is needed as the two-pointer solution is optimal.

---

### Problem 10: Reorder List

#### Problem Understanding:

- **Problem Explanation**: Given a singly linked list `L: L0 → L1 → … → Ln-1 → Ln`, reorder it to: `L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …`

You must do this in-place without altering the nodes' values.

**Example**:
Input: `head = [1, 2, 3, 4]`
Output: `[1, 4, 2, 3]`

#### Coding Pattern:

- This problem can be solved in three steps:
  1. **Split the list** into two halves.
  2. **Reverse the second half** of the list.
  3. **Merge** the two halves in alternating fashion.

#### Solution:

```python
def reorder_list(head):
    if not head:
        return
  
    # Step 1: Find the middle of the list using the slow-fast pointer approach
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
  
    # Step 2: Reverse the second half of the list
    prev, curr = None, slow
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp
  
    # Step 3: Merge the two halves
    first, second = head, prev
    while second.next:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first = tmp1
        second = tmp2

# Time Complexity: O(n) - we traverse the list multiple times (split, reverse, merge)
# Space Complexity: O(1) - constant space for pointer manipulation

# Test the function with example linked lists (you can create linked list test cases)
```

#### Alternative Approach:

- **No alternative approach** is needed as this three-step approach is optimal for reordering in place.

---

### Problem 11: Remove Nth Node From End of List

#### Problem Understanding:

- **Problem Explanation**: Given the head of a linked list, remove the nth node from the end of the list and return its head.

**Example**:
Input: `head = [1, 2, 3, 4, 5]`, `n = 2`
Output: `[1, 2, 3, 5]`

#### Coding Pattern:

- This problem can be solved using the **Two Pointers** approach. One pointer will be ahead of the other by `n` steps, so when the first pointer reaches the end, the second pointer will be at the node to remove.

#### Solution:

```python
def remove_nth_from_end(head, n):
    dummy = ListNode(0)  # Create a dummy node before the head
    dummy.next = head
    first = dummy
    second = dummy
  
    # Move the first pointer so that it's `n` nodes ahead
    for _ in range(n + 1):
        first = first.next
  
    # Move both pointers until first reaches the end
    while first:
        first = first.next
        second = second.next
  
    # Second pointer is now at the node before the one to remove
    second.next = second.next.next
  
    return dummy.next  # Return the modified list

# Time Complexity: O(n) - we traverse the list twice (move pointers and remove node)
# Space Complexity: O(1) - constant space for pointer manipulation

# Test the function with example linked lists
```

#### Alternative Approach:

- **No alternative approach** is needed as the two-pointer approach is efficient and intuitive.

---

### Problem 12: Copy List with Random Pointer

#### Problem Understanding:

- **Problem Explanation**: A linked list is given where each node contains an additional random pointer which could point to any node in the list or `None`. You need to make a deep copy of this list.

**Example**:
Input: `head = [[7,null],[13,0],[11,4],[10,2],[1,0]]`
Output: `[[7,null],[13,0],[11,4],[10,2],[1,0]]` (a deep copy of the original list).

#### Coding Pattern:

- This problem can be solved in two steps:
  1. Create new nodes interleaved with the old nodes.
  2. Assign the `random` pointers to the new nodes and then restore the original list.

#### Solution:

```python
class Node:
    def __init__(self, val, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

def copy_random_list(head):
    if not head:
        return None
  
    # Step 1: Create new nodes interleaved with the original ones
    curr = head
    while curr:
        new_node = Node(curr.val)
        new_node.next = curr.next
        curr.next = new_node
        curr = new_node.next
  
    # Step 2: Assign random pointers for the copied nodes
    curr = head
    while curr:
        if curr.random:
            curr.next.random = curr.random.next
        curr = curr.next.next
  
    # Step 3: Separate the original and copied nodes
    curr = head
    copy_head = head.next
    copy_curr = copy_head
    while curr:
        curr.next = curr.next.next
        if copy_curr.next:
            copy_curr.next = copy_curr.next.next
        curr = curr.next
        copy_curr = copy_curr.next
  
    return copy_head

# Time Complexity: O(n) - where n is the number of nodes in the list
# Space Complexity: O(1) - interleaving the nodes uses constant space

# Test the function with example linked lists
```

#### Alternative Approach:

- **No alternative approach** is necessary, as this method solves the problem in O(n) time without additional space beyond the copied nodes.

---

### Problem 13: Add Two Numbers

#### Problem Understanding:

- **Problem Explanation**: Given two non-empty linked lists representing two non-negative integers, add the two numbers and return the sum as a linked list. The digits are stored in reverse order.

**Example**:
Input: `l1 = [2, 4, 3]`, `l2 = [5, 6, 4]`
Output: `[7, 0, 8]` (since 342 + 465 = 807).

#### Coding Pattern:

- This problem can be solved by **Simulating the Addition** of two numbers, carrying over any value greater than 9.

#### Solution:

```python
def add_two_numbers(l1, l2):
    dummy = ListNode()
    current = dummy
    carry = 0
  
    # Traverse both lists until both are empty
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        total = val1 + val2 + carry
        carry = total // 10  # Calculate carry for the next digit
        current.next = ListNode(total % 10)  # Create the new node with the current digit
        current = current.next
      
        # Move to the next nodes
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
  
    return dummy.next

# Time Complexity: O(max(n, m)) - where n and m are the lengths of the two lists
# Space Complexity: O(max(n, m)) - for the new linked list storing the sum

# Test the function with example linked lists
```

#### Alternative Approach:

- **No alternative approach** is needed, as this straightforward addition method works efficiently.

---

### Problem 14: Linked List Cycle

#### Problem Understanding:

- **Problem Explanation**: Given a linked list, determine if it has a cycle in it.

**Example**:
Input: `head = [3,2,0,-4]` (with a cycle)
Output: `True`

#### Coding Pattern:

- This problem can be solved using the **Floyd's Tortoise and Hare** algorithm. We use two pointers (slow and fast). If there is a cycle, they will eventually meet.

#### Solution:

```python
def has_cycle(head):
    slow = fast = head
  
    # Move slow by one step and fast by two steps
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
      
        # If they meet, there is a cycle
        if slow == fast:
            return True
  
    return False  # No cycle detected

# Time Complexity: O(n) - we traverse the list with two pointers
# Space Complexity: O(1) - constant space for the two pointers

# Test the function with example linked lists
```

#### Alternative Approach:

- **No alternative approach** is needed, as Floyd's cycle detection algorithm is optimal.

---

### Problem 15: Find the Duplicate Number

#### Problem Understanding:

- **Problem Explanation**: Given an array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]` inclusive, return the duplicate number. There is only one repeated number in `nums`.

**Example**:
Input: `nums = [1, 3, 4, 2, 2]`
Output: `2`

#### Coding Pattern:

- This problem can be solved using the **Floyd's Tortoise and Hare** (Cycle Detection) algorithm, as the array can be viewed as a linked list where each number points to the index of the next number.

#### Solution:

```python
def find_duplicate(nums):
    # Step 1: Use Floyd's Tortoise and Hare algorithm to detect the cycle
    slow = fast = nums[0]
  
    # Move slow by one step and fast by two steps
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
  
    # Step 2: Find the entrance to the cycle (the duplicate number)
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
  
    return slow

# Time Complexity: O(n) - where n is the number of elements in the array
# Space Complexity: O(1) - constant space used for the pointers

# Test the function with the example
print(find_duplicate([1, 3, 4, 2, 2]))  # Output: 2
```

#### Alternative Approach:

- **No alternative approach** is needed, as Floyd’s Tortoise and Hare algorithm is optimal for finding duplicates in this problem.

---

### Problem 16: LRU Cache

#### Problem Understanding:

- **Problem Explanation**: Design a data structure that follows the constraints of a **Least Recently Used (LRU) Cache**. Implement the `LRUCache` class with the following operations:
  - `get(key)`: Return the value of the key if it exists, otherwise return `-1`.
  - `put(key, value)`: Insert the key-value pair if it doesn't exist. If the cache exceeds its capacity, remove the least recently used item.

**Example**:

```
LRUCache cache = new LRUCache(2); // Capacity is 2
cache.put(1, 1);
cache.put(2, 2);
cache.get(1); // returns 1
cache.put(3, 3); // evicts key 2
cache.get(2); // returns -1
```

#### Coding Pattern:

- This problem can be solved using a combination of a **HashMap** (for quick access) and a **Doubly Linked List** (for tracking the order of use).

#### Solution:

```python
class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # HashMap to store keys and their corresponding nodes
        self.head = Node()  # Dummy head
        self.tail = Node()  # Dummy tail
        self.head.next = self.tail  # Initialize head and tail to point to each other
        self.tail.prev = self.head

    def _remove(self, node):
        """Remove a node from the doubly linked list."""
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev

    def _add(self, node):
        """Add a node right after the head."""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)  # Move accessed node to the front
            self._add(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key, value)
        self._add(node)
        self.cache[key] = node
        if len(self.cache) > self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]

# Time Complexity: O(1) for both get and put operations
# Space Complexity: O(capacity) - for storing the cache and doubly linked list

# Test the LRU Cache
cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))  # Output: 1
cache.put(3, 3)  # Evicts key 2
print(cache.get(2))  # Output: -1
```

#### Alternative Approach:

- **No alternative approach** is needed, as using a combination of a HashMap and Doubly Linked List is optimal.

---

### Problem 17: Merge K Sorted Lists

#### Problem Understanding:

- **Problem Explanation**: Given an array of `k` linked lists, each list is sorted in ascending order, merge all the lists into one sorted linked list and return it.

**Example**:
Input: `lists = [[1,4,5],[1,3,4],[2,6]]`
Output: `[1,1,2,3,4,4,5,6]`

#### Coding Pattern:

- This problem can be solved using a **Min-Heap** (or priority queue) to efficiently merge the lists by always choosing the smallest element from the available heads of the lists.

#### Solution:

```python
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_k_lists(lists):
    # Create a min-heap
    min_heap = []
  
    # Add the head of each list to the heap
    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(min_heap, (lists[i].val, i, lists[i]))
  
    dummy = ListNode()
    current = dummy
  
    # Extract the smallest element and add the next node from that list to the heap
    while min_heap:
        val, i, node = heapq.heappop(min_heap)
        current.next = node
        current = current.next
        if node.next:
            heapq.heappush(min_heap, (node.next.val, i, node.next))
  
    return dummy.next

# Time Complexity: O(N log k) - where N is the total number of nodes and k is the number of lists
# Space Complexity: O(k) - for the heap storing the heads of k lists

# Test the function with example linked lists
```

#### Alternative Approach:

- **No alternative approach** is required, as the heap-based solution efficiently solves the problem in O(N log k) time.

---

### Problem 18: Reverse Nodes in k-Group

#### Problem Understanding:

- **Problem Explanation**: Given a linked list, reverse the nodes of a linked list `k` at a time, and return its modified list. If the number of nodes is not a multiple of `k`, leave the last nodes as they are.

**Example**:
Input: `head = [1, 2, 3, 4, 5]`, `k = 2`
Output: `[2, 1, 4, 3, 5]`

#### Coding Pattern:

- This problem can be solved by **Reversing Nodes in Groups**. First, find the length of the list, then reverse nodes in chunks of size `k`.

#### Solution:

```python
def reverse_k_group(head, k):
    def reverse_linked_list(start, end):
        """Reverse the linked list from start to end."""
        prev, curr = None, start
        while curr != end:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev
  
    dummy = ListNode(0)
    dummy.next = head
    group_prev = dummy
  
    while True:
        kth_node = group_prev
        for _ in range(k):
            kth_node = kth_node.next
            if not kth_node:
                return dummy.next
      
        group_next = kth_node.next
        # Reverse the k nodes
        prev, curr = group_prev.next, group_prev.next.next
        for _ in range(k - 1):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
      
        temp = group_prev.next
        group_prev.next.next = group_next
        group_prev.next = prev
        group_prev = temp

# Time Complexity: O(n) - where n is the number of nodes in the list
# Space Complexity: O(1) - constant space for pointer manipulation

# Test the function with example linked lists
```

#### Alternative Approach:

- **No alternative approach** is necessary as the iterative reversal method is efficient.

---

## Trees Section

### Problem 19: Invert Binary Tree

#### Problem Understanding:

- **Problem Explanation**: Invert a binary tree.

**Example**:
Input:

```
    4
   / \
  2   7
 / \ / \
1  3 6  9
```

Output:

```
    4
   / \
  7   2
 / \ / \
9  6 3  1
```

#### Coding Pattern:

- This problem can be solved recursively or iteratively by swapping the left and right children of each node.

#### Solution (Recursive):

```python
def invert_tree(root):
    if not root:
        return None
  
    # Swap the left and right children
    root.left, root.right = root.right, root.left
  
    # Recursively invert the subtrees
    invert_tree(root.left)
    invert_tree(root.right)
  
    return root

# Time Complexity: O(n) - where n is the number of nodes in the tree
# Space Complexity: O(h) - where h is the height of the tree (recursion stack)

# Test the function with a binary tree
```

#### Alternative Approach:

- **Iterative Approach** using a queue to perform level-order traversal and swap children at each level.

```python
from collections import deque

def invert_tree_iterative(root):
    if not root:
        return None
  
    queue = deque([root])
  
    while queue:
        node = queue.popleft()
        # Swap the children
        node.left, node.right = node.right, node.left
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
  
    return root
```

---

### Problem 20: Maximum Depth of Binary Tree

#### Problem Understanding:

- **Problem Explanation**: Given the root of a binary tree, return its maximum depth. The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

**Example**:
Input:

```
    3
   / \
  9   20
     /  \
    15   7
```

Output: `3`

#### Coding Pattern:

- This problem can be solved using **Recursion** (depth-first search) or **Breadth-First Search** (level-order traversal).

#### Solution (Recursive):

```python
def max_depth(root):
    if not root:
        return 0
    # The depth is the maximum of the left and right subtrees, plus 1 for the root
    return 1 + max(max_depth(root.left), max_depth(root.right))

# Time Complexity: O(n) - where n is the number of nodes in the tree
# Space Complexity: O(h) - where h is the height of the tree (recursion stack)

# Test the function with a binary tree
```

#### Alternative Approach (Iterative):

```python
from collections import deque

def max_depth_iterative(root):
    if not root:
        return 0
  
    queue = deque([root])
    depth = 0
  
    # Perform level-order traversal (BFS)
    while queue:
        depth += 1
        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
  
    return depth

# Time Complexity: O(n) - where n is the number of nodes in the tree
# Space Complexity: O(n) - for the queue used in BFS
```

---

### Problem 21: Diameter of Binary Tree

#### Problem Understanding:

- **Problem Explanation**: Given the root of a binary tree, return the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

**Example**:
Input:

```
    1
   / \
  2   3
 / \   
4   5  
```

Output: `3` (the longest path is [4,2,1,3] or [5,2,1,3], and the length is 3).

#### Coding Pattern:

- This problem can be solved using **Recursion** (Depth-First Search). The diameter at any node is the sum of the heights of its left and right subtrees.

#### Solution:

```python
def diameter_of_binary_tree(root):
    diameter = 0
  
    def depth(node):
        nonlocal diameter
        if not node:
            return 0
        # Recursively find the depth of the left and right subtrees
        left_depth = depth(node.left)
        right_depth = depth(node.right)
        # Update the diameter (maximum path length at this node)
        diameter = max(diameter, left_depth + right_depth)
        # Return the depth of the tree at this node
        return 1 + max(left_depth, right_depth)
  
    depth(root)
    return diameter

# Time Complexity: O(n) - where n is the number of nodes in the tree
# Space Complexity: O(h) - where h is the height of the tree (recursion stack)

# Test the function with a binary tree
```

#### Alternative Approach:

- **No alternative approach** is necessary, as this solution is optimal.

---

### Problem 22: Balanced Binary Tree

#### Problem Understanding:

- **Problem Explanation**: Given the root of a binary tree, determine if it is height-balanced. A height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differs by more than 1.

**Example**:
Input:

```
    3
   / \
  9  20
     /  \
    15   7
```

Output: `True`

#### Coding Pattern:

- This problem can be solved using **Recursion** (Depth-First Search) to check the height of the left and right subtrees and ensure the difference is not greater than 1.

#### Solution:

```python
def is_balanced(root):
    def height(node):
        if not node:
            return 0
        # Check the height of the left and right subtrees
        left_height = height(node.left)
        right_height = height(node.right)
      
        # If any subtree is unbalanced, return -1
        if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
            return -1
        return 1 + max(left_height, right_height)
  
    # If height returns -1, the tree is not balanced
    return height(root) != -1

# Time Complexity: O(n) - where n is the number of nodes in the tree
# Space Complexity: O(h) - where h is the height of the tree (recursion stack)

# Test the function with a binary tree
```

#### Alternative Approach:

- **No alternative approach** is necessary, as this solution efficiently checks the balance condition.

---

### Problem 23: Same Tree

#### Problem Understanding:

- **Problem Explanation**: Given the roots of two binary trees, determine if they are the same. Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

**Example**:
Input:

```
    Tree 1:
        1
       / \
      2   3
    Tree 2:
        1
       / \
      2   3
```

Output: `True`

#### Coding Pattern:

- This problem can be solved using **Recursion** to compare both trees node by node.

#### Solution:

```python
def is_same_tree(p, q):
    # If both nodes are None, they are the same
    if not p and not q:
        return True
    # If one node is None and the other is not, they are different
    if not p or not q:
        return False
    # If the values of the nodes are different, they are different
    if p.val != q.val:
        return False
    # Recursively check the left and right subtrees
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

# Time Complexity: O(n) - where n is the number of nodes in the smaller tree
# Space Complexity: O(h) - where h is the height of the tree (recursion stack)

# Test the function with two binary trees
```

#### Alternative Approach:

- **No alternative approach** is needed, as this recursive solution efficiently compares the trees.

---

### Problem 24: Subtree of Another Tree

#### Problem Understanding:

- **Problem Explanation**: Given two binary trees `root` and `subRoot`, return `True` if there is a subtree of `root` that is identical to `subRoot`. A subtree of a binary tree is a tree that consists of a node and all its descendants.

**Example**:
Input:

```
    Root:
        3
       / \
      4   5
     / \
    1   2

    SubRoot:
        4
       / \
      1   2
```

Output: `True`

#### Coding Pattern:

- This problem can be solved using **Recursion**. For each node in the main tree, we check if the subtree rooted at that node is identical to the `subRoot`.

#### Solution:

```python
def is_subtree(root, sub_root):
    if not root:
        return False
    if is_same_tree(root, sub_root):
        return True
    # Recursively check the left and right subtrees
    return is_subtree(root.left, sub_root) or is_subtree(root.right, sub_root)

# Helper function to check if two trees are the same (as defined in the previous problem)
def is_same_tree(p, q):
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

# Time Complexity: O(m * n) - where m is the number of nodes in the main tree and n is the number of nodes in the subtree
# Space Complexity: O(h) - where h is the height of the main tree (recursion stack)

# Test the function with two binary trees
```

#### Alternative Approach:

- **No alternative approach** is required, as the recursive solution checks all potential subtrees efficiently.

---

### Problem 25: Lowest Common Ancestor of a Binary Search Tree

#### Problem Understanding:

- **Problem Explanation**: Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes. The LCA is defined as the lowest node that has both nodes as descendants.

**Example**:
Input:

```
    6
   / \
  2   8
 / \ / \
0  4 7  9
```

Nodes: `2` and `8`
Output: `6`

#### Coding Pattern:

- This problem can be solved using **Recursion** or **Iteration**. Since it's a BST, we can take advantage of its properties

 to decide whether to go left or right.

#### Solution:

```python
def lowest_common_ancestor(root, p, q):
    # If both nodes are larger than the current node, go to the right subtree
    if p.val > root.val and q.val > root.val:
        return lowest_common_ancestor(root.right, p, q)
    # If both nodes are smaller than the current node, go to the left subtree
    elif p.val < root.val and q.val < root.val:
        return lowest_common_ancestor(root.left, p, q)
    # Otherwise, the current node is the LCA
    else:
        return root

# Time Complexity: O(h) - where h is the height of the tree
# Space Complexity: O(h) - for the recursion stack

# Test the function with a binary search tree
```

#### Alternative Approach (Iterative):

```python
def lowest_common_ancestor_iterative(root, p, q):
    while root:
        if p.val > root.val and q.val > root.val:
            root = root.right
        elif p.val < root.val and q.val < root.val:
            root = root.left
        else:
            return root
```

---

### Problem 26: Binary Tree Level Order Traversal

#### Problem Understanding:

- **Problem Explanation**: Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

**Example**:
Input:

```
    3
   / \
  9  20
     /  \
    15   7
```

Output: `[[3], [9, 20], [15, 7]]`

#### Coding Pattern:

- This problem can be solved using **Breadth-First Search (BFS)** or **Level Order Traversal** with a queue.

#### Solution:

```python
from collections import deque

def level_order(root):
    if not root:
        return []
  
    result = []
    queue = deque([root])
  
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
  
    return result

# Time Complexity: O(n) - where n is the number of nodes in the tree
# Space Complexity: O(n) - for storing nodes in the queue

# Test the function with a binary tree
```

#### Alternative Approach:

- **No alternative approach** is necessary, as BFS is the optimal solution for level order traversal.

---

### Problem 27: Binary Tree Right Side View

#### Problem Understanding:

- **Problem Explanation**: Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

**Example**:
Input:

```
    1
   / \
  2   3
   \   \
    5   4
```

Output: `[1, 3, 4]`

#### Coding Pattern:

- This problem can be solved using **Level Order Traversal** and capturing the last element of each level (which is the rightmost node).

#### Solution:

```python
from collections import deque

def right_side_view(root):
    if not root:
        return []
  
    result = []
    queue = deque([root])
  
    while queue:
        rightmost_node = None
        for _ in range(len(queue)):
            node = queue.popleft()
            rightmost_node = node  # Update to the last node at this level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(rightmost_node.val)  # The rightmost node for this level
  
    return result

# Time Complexity: O(n) - where n is the number of nodes in the tree
# Space Complexity: O(n) - for storing nodes in the queue

# Test the function with a binary tree
```

#### Alternative Approach:

- **DFS (Depth-First Search)** can also be used by visiting right children first and ensuring we add only the first node at each depth.

---

### Problem 28: Count Good Nodes in Binary Tree

#### Problem Understanding:

- **Problem Explanation**: Given a binary tree root, a node X in the tree is named **good** if in the path from the root to X there are no nodes with a value greater than X. Return the number of good nodes in the binary tree.

**Example**:
Input:

```
    3
   / \
  1   4
     / \
    1   5
```

Output: `4` (good nodes are 3, 4, 5, and 3 itself).

#### Coding Pattern:

- This problem can be solved using **DFS (Depth-First Search)** where, at each node, we check if the current node is greater than or equal to the maximum value seen so far in the path.

#### Solution:

```python
def good_nodes(root):
    def dfs(node, max_val):
        if not node:
            return 0
        # Count the current node as good if its value is greater than or equal to max_val
        count = 1 if node.val >= max_val else 0
        max_val = max(max_val, node.val)
        # Recursively count good nodes in the left and right subtrees
        count += dfs(node.left, max_val)
        count += dfs(node.right, max_val)
        return count
  
    return dfs(root, root.val)

# Time Complexity: O(n) - where n is the number of nodes in the tree
# Space Complexity: O(h) - where h is the height of the tree (recursion stack)

# Test the function with a binary tree
```

#### Alternative Approach:

- **No alternative approach** is needed, as this DFS-based solution is optimal.

---

### Problem 29: Validate Binary Search Tree

#### Problem Understanding:

- **Problem Explanation**: Given the root of a binary tree, determine if it is a valid binary search tree (BST). A valid BST is defined as follows:
  - The left subtree of a node contains only nodes with keys less than the node's key.
  - The right subtree of a node contains only nodes with keys greater than the node's key.
  - Both the left and right subtrees must also be binary search trees.

**Example**:
Input:

```
    2
   / \
  1   3
```

Output: `True`

#### Coding Pattern:

- This problem can be solved using **Recursion** by ensuring that each node satisfies the BST property, i.e., its value is greater than the allowed minimum and less than the allowed maximum.

#### Solution:

```python
def is_valid_bst(root):
    def validate(node, low=float('-inf'), high=float('inf')):
        if not node:
            return True
        # The current node's value must be between low and high
        if node.val <= low or node.val >= high:
            return False
        # Recursively validate the left and right subtrees
        return validate(node.left, low, node.val) and validate(node.right, node.val, high)
  
    return validate(root)

# Time Complexity: O(n) - where n is the number of nodes in the tree
# Space Complexity: O(h) - where h is the height of the tree (recursion stack)

# Test the function with a binary tree
```

#### Alternative Approach:

- **In-order traversal** can also be used, where we ensure the values are visited in increasing order.

---

### Problem 30: Kth Smallest Element in a BST

#### Problem Understanding:

- **Problem Explanation**: Given the root of a binary search tree, and an integer `k`, return the `k`th smallest element in the BST.

**Example**:
Input:

```
    3
   / \
  1   4
   \
    2
```

k = 1
Output: `1`

#### Coding Pattern:

- This problem can be solved using **In-Order Traversal** (which visits nodes in ascending order in a BST) and tracking the count of nodes visited.

#### Solution:

```python
def kth_smallest(root, k):
    def inorder(node):
        if not node:
            return []
        return inorder(node.left) + [node.val] + inorder(node.right)
  
    # Perform an in-order traversal and get the k-th smallest element
    return inorder(root)[k - 1]

# Time Complexity: O(n) - where n is the number of nodes in the tree (we visit each node)
# Space Complexity: O(n) - for storing the inorder traversal list

# Test the function with a binary search tree
```

#### Alternative Approach:

- **Iterative In-order Traversal** can be used with a stack to reduce the space complexity to O(h) where h is the height of the tree.

---

### Problem 31: Construct Binary Tree from Preorder and Inorder Traversal

#### Problem Understanding:

- **Problem Explanation**: Given two integer arrays `preorder` and `inorder` where `preorder` is the preorder traversal of a binary tree and `inorder` is the inorder traversal of the same tree, construct and return the binary tree.

**Example**:
Input:

```
Preorder = [3,9,20,15,7]  
Inorder = [9,3,15,20,7]
```

Output:

```
    3
   / \
  9  20
     / \
    15  7
```

#### Coding Pattern:

- This problem can be solved using **Recursion**. The first element of the preorder array is the root, and we can find the root in the inorder array to split it into left and right subtrees.

#### Solution:

```python
def build_tree(preorder, inorder):
    if not preorder or not inorder:
        return None
  
    # The first element in preorder is the root
    root_val = preorder.pop(0)
    root = TreeNode(root_val)
  
    # Find the root in inorder to split the tree into left and right subtrees
    inorder_index = inorder.index(root_val)
  
    # Recursively build the left and right subtrees
    root.left = build_tree(preorder, inorder[:inorder_index])
    root.right = build_tree(preorder, inorder[inorder_index + 1:])
  
    return root

# Time Complexity: O(n^2) - for each node, we need to search in the inorder array
# Space Complexity: O(n) - for the recursion stack and

 new tree nodes

# Test the function with preorder and inorder arrays
```

#### Alternative Approach:

- **Optimized Approach**: Use a hashmap to store the indices of inorder elements for O(1) lookup, reducing the time complexity to O(n).

---

### Problem 32: Binary Tree Maximum Path Sum

#### Problem Understanding:

- **Problem Explanation**: Given a non-empty binary tree, return the maximum path sum. A path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections.

**Example**:
Input:

```
    1
   / \
  2   3
```

Output: `6` (1 → 2 → 3)

#### Coding Pattern:

- This problem can be solved using **Recursion**. At each node, we calculate the maximum path sum that includes the current node and potentially its children.

#### Solution:

```python
def max_path_sum(root):
    max_sum = float('-inf')
  
    def dfs(node):
        nonlocal max_sum
        if not node:
            return 0
        # Compute the maximum sum on the left and right, ignoring negative sums
        left_sum = max(dfs(node.left), 0)
        right_sum = max(dfs(node.right), 0)
      
        # Update the global maximum path sum that passes through the current node
        max_sum = max(max_sum, node.val + left_sum + right_sum)
      
        # Return the maximum path sum with the current node as the endpoint
        return node.val + max(left_sum, right_sum)
  
    dfs(root)
    return max_sum

# Time Complexity: O(n) - where n is the number of nodes in the tree
# Space Complexity: O(h) - where h is the height of the tree (recursion stack)

# Test the function with a binary tree
```

---

### Problem 33: Serialize and Deserialize Binary Tree

#### Problem Understanding:

- **Problem Explanation**: Design an algorithm to serialize and deserialize a binary tree. Serialization is the process of converting a tree into a string, and deserialization is converting the string back to a tree.

**Example**:
Input:

```
    1
   / \
  2   3
     / \
    4   5
```

Output: `1,2,3,null,null,4,5` (Serialized form)

#### Coding Pattern:

- We can solve this problem using **Preorder Traversal** to serialize and deserialize the tree.

#### Solution:

```python
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string."""
        def preorder(node):
            if not node:
                return "null,"
            return str(node.val) + "," + preorder(node.left) + preorder(node.right)
      
        return preorder(root)

    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        def build(nodes):
            val = nodes.pop(0)
            if val == "null":
                return None
            node = TreeNode(int(val))
            node.left = build(nodes)
            node.right = build(nodes)
            return node
      
        node_list = data.split(',')
        return build(node_list)

# Time Complexity: O(n) - where n is the number of nodes in the tree
# Space Complexity: O(n) - for storing the serialized data and the recursion stack

# Test the Codec class with a binary tree
```

---

## Heap / Priority Queue Section

### Problem 1: Kth Largest Element in a Stream

#### Problem Understanding:

- **Problem Explanation**: Design a class that finds the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement the `KthLargest` class:

- `KthLargest(int k, int[] nums)`: Initializes the object with the integer `k` and the stream of integers `nums`.
- `int add(int val)`: Appends the integer `val` to the stream and returns the element representing the kth largest element.

**Example**:

```
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // returns 4
kthLargest.add(5);   // returns 5
kthLargest.add(10);  // returns 5
kthLargest.add(9);   // returns 8
kthLargest.add(4);   // returns 8
```

#### Coding Pattern:

- This problem can be solved using a **Min-Heap**. We maintain a heap of size `k`, where the smallest element in the heap will always represent the kth largest element.

#### Solution:

```python
import heapq

class KthLargest:
    def __init__(self, k: int, nums: list):
        # Initialize the heap and maintain the size as k
        self.k = k
        self.min_heap = nums
        heapq.heapify(self.min_heap)  # Convert nums into a heap
        # Reduce the size of the heap to k by popping the smallest elements
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        # Add the new value to the heap
        heapq.heappush(self.min_heap, val)
        # If the size of the heap exceeds k, pop the smallest element
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        # The kth largest element is always at the root of the heap
        return self.min_heap[0]

# Time Complexity: O(log k) for adding elements (maintaining the heap)
# Space Complexity: O(k) for storing the k largest elements in the heap

# Test case
kthLargest = KthLargest(3, [4, 5, 8, 2])
print(kthLargest.add(3))  # Output: 4
print(kthLargest.add(5))  # Output: 5
print(kthLargest.add(10))  # Output: 5
print(kthLargest.add(9))  # Output: 8
print(kthLargest.add(4))  # Output: 8
```

---

### Problem 2: Last Stone Weight

#### Problem Understanding:

- **Problem Explanation**: You are given an array of integers `stones` where each stone represents the weight of a stone. In each turn, you select the two heaviest stones and smash them together. Suppose the stones have weights `x` and `y` with `x <= y`. The result of this smash is:
  - If `x == y`, both stones are destroyed.
  - If `x != y`, the stone with weight `y - x` remains.
    Repeat this process until at most one stone remains. Return the weight of the last remaining stone, or 0 if no stones remain.

**Example**:
Input: `stones = [2,7,4,1,8,1]`
Output: `1`

#### Coding Pattern:

- This problem can be solved using a **Max-Heap** (in Python, we simulate a max-heap by using negative values in a min-heap).

#### Solution:

```python
import heapq

def last_stone_weight(stones):
    # Convert all stones into negative values to simulate a max-heap
    stones = [-stone for stone in stones]
    heapq.heapify(stones)  # Turn the list into a heap
  
    # Process the stones until there is at most one stone left
    while len(stones) > 1:
        # Pop the two largest stones (remember they are negative, so we negate them)
        stone1 = -heapq.heappop(stones)
        stone2 = -heapq.heappop(stones)
      
        # If they are not equal, push the difference back into the heap
        if stone1 != stone2:
            heapq.heappush(stones, -(stone1 - stone2))
  
    # If there is no stone left, return 0, else return the last remaining stone
    return -stones[0] if stones else 0

# Time Complexity: O(n log n) - where n is the number of stones, since each operation on the heap is log n
# Space Complexity: O(n) - for storing the heap

# Test case
print(last_stone_weight([2, 7, 4, 1, 8, 1]))  # Output: 1
```

---

### Problem 3: K Closest Points to Origin

#### Problem Understanding:

- **Problem Explanation**: Given an array of points where `points[i] = [xi, yi]` represents a point on the X-Y plane and an integer `k`, return the `k` closest points to the origin `(0, 0)`.

The distance between two points on the X-Y plane is the Euclidean distance. You may return the answer in any order.

**Example**:
Input: `points = [[1,3],[-2,2]]`, `k = 1`
Output: `[[-2, 2]]`

#### Coding Pattern:

- This problem can be solved using a **Max-Heap** to store the closest `k` points.

#### Solution:

```python
import heapq
import math

def k_closest(points, k):
    # Max-heap to store the k closest points
    max_heap = []
  
    for point in points:
        x, y = point
        # Calculate the squared distance from the origin (to avoid float precision issues)
        dist = -(x ** 2 + y ** 2)  # We use negative to simulate a max-heap
        # Push the point into the heap
        heapq.heappush(max_heap, (dist, point))
      
        # If the heap exceeds size k, remove the farthest point
        if len(max_heap) > k:
            heapq.heappop(max_heap)
  
    # Extract the points from the heap
    return [point for _, point in max_heap]

# Time Complexity: O(n log k) - where n is the number of points, and k is the number of closest points
# Space Complexity: O(k) - for storing the k closest points in the heap

# Test case
print(k_closest([[1, 3], [-2, 2], [5, 8], [0, 1]], 2))  # Output: [[-2, 2], [0, 1]]
```

---

### Problem 4: Kth Largest Element in an Array

#### Problem Understanding:

- **Problem Explanation**: Given an integer array `nums` and an integer `k`, return the `k`th largest element in the array.

**Example**:
Input: `nums = [3,2,3,1,2,4,5,5,6]`, `k = 4`
Output: `4`

#### Coding Pattern:

- This problem can be solved using a **Min-Heap**. We maintain a heap of size `k`, and the top of the heap will always represent the `k`th largest element.

#### Solution:

```python
import heapq

def find_kth_largest(nums, k):
    # Initialize a min-heap with the first k elements
    min_heap = nums[:k]
    heapq.heapify(min_heap)  # Convert to a heap
  
    # Process the remaining elements in the array
    for num in nums[k:]:
        # If the current number is greater than the smallest in the heap, replace it
        if num > min_heap[0]:
            heapq.heapreplace(min_heap, num)
  
    # The top of the heap is the kth largest element
    return min_heap[0]

# Time Complexity: O(n log k) - we process n elements and maintain a heap of size k
# Space Complexity: O(k) - for storing the k largest elements in the heap

# Test case
print(find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))  # Output: 4
```

---

### Problem 5: Task Scheduler

#### Problem Understanding:

- **Problem Explanation**: You are given a char array representing tasks, where each letter represents a different task. Tasks must be done in order, but there is a cooldown period `n` after each task is performed. You must wait `n` intervals before performing the same task again. You need to return the least number of intervals required to complete all the tasks.

**Example**:
Input: `tasks = ["A","A","A","B","B","B"]`, `n = 2`
Output: `8`
Explanation: The task execution sequence can be "A -> B -> idle -> A -> B -> idle -> A -> B".

#### Coding Pattern:

- This problem can be solved using a **Priority Queue (Max-Heap)** to always schedule the most frequent tasks first.

#### Solution:

```python
import heapq
from collections import Counter

def least_interval(tasks, n):
    # Step 1: Count the frequency of each task
    task_counts = Counter(tasks)
  
    # Step 2: Create a max-heap (invert counts to simulate max-heap in Python's min-heap)
    max_heap = [-count for count in task_counts.values()]
    heapq.heapify(max_heap)  # Heapify the list of counts
  
    time = 0  # To track the total intervals
    while max_heap:
        i = 0  # Initialize the cycle for the interval
        temp = []  # Temporary storage for tasks that still need to be completed
      
        # Step 3: Schedule up to 'n + 1' tasks (cooldown period)
        while i <= n:
            if max_heap:
                # Pop the most frequent task (invert back since heap is negative)
                task = heapq.heappop(max_heap)
                if task < -1:
                    # If there's still more of this task to process, reduce count and store temporarily
                    temp.append(task + 1)
            time += 1  # Count the time intervals
            if not max_heap and not temp:
                break  # If no more tasks are left, break out of the loop
            i += 1
      
        # Step 4: Push remaining tasks back into the heap
        for task in temp:
            heapq.heappush(max_heap, task)
  
    return time

# Time Complexity: O(n log k) - where n is the total number of tasks, and k is the number of unique tasks
# Space Complexity: O(k) - where k is the number of unique tasks in the heap

# Test the function with the example
print(least_interval(["A", "A", "A", "B", "B", "B"], 2))  # Output: 8
```

---

### Problem 6: Design Twitter

#### Problem Understanding:

- **Problem Explanation**: Design a simplified version of Twitter where users can post tweets, follow/unfollow others, and see the 10 most recent tweets in their news feed.

Implement the `Twitter` class:

- `postTweet(userId, tweetId)`: Composes a new tweet.
- `getNewsFeed(userId)`: Retrieves the 10 most recent tweet ids in the user's news feed.
- `follow(followerId, followeeId)`: Follower follows a followee.
- `unfollow(followerId, followeeId)`: Follower unfollows a followee.

**Example**:

```
Twitter twitter = new Twitter();
twitter.postTweet(1, 5);
twitter.getNewsFeed(1);  // returns [5]
twitter.follow(1, 2);
twitter.postTweet(2, 6);
twitter.getNewsFeed(1);  // returns [6, 5]
twitter.unfollow(1, 2);
twitter.getNewsFeed(1);  // returns [5]
```

#### Coding Pattern:

- This problem can be solved using a **HashMap** (to store user tweets and relationships) and a **Min-Heap** (to keep track of the 10 most recent tweets).

#### Solution:

```python
import heapq
from collections import defaultdict, deque

class Twitter:

    def __init__(self):
        # Tweet storage (userId -> deque of tweets (tweetId, timestamp))
        self.user_tweets = defaultdict(deque)
        # User following relationships (follower -> set of followees)
        self.user_follows = defaultdict(set)
        self.time = 0  # Global timestamp for tweets (to maintain order)

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Add the tweet to the user's deque (use deque to efficiently manage recent tweets)
        self.user_tweets[userId].appendleft((tweetId, self.time))
        self.time += 1  # Increment the global time
  
    def getNewsFeed(self, userId: int) -> list:
        # Get the recent tweets from the user and all followees
        tweet_candidates = list(self.user_tweets[userId])  # Start with user's own tweets
      
        # Include tweets from followees
        for followee in self.user_follows[userId]:
            tweet_candidates.extend(self.user_tweets[followee])
      
        # Use a heap to get the 10 most recent tweets
        return [tweet[0] for tweet in heapq.nlargest(10, tweet_candidates, key=lambda x: x[1])]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.user_follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.user_follows[followerId].discard(followeeId)

# Time Complexity: 
# - postTweet: O(1) - adding to a deque is O(1)
# - getNewsFeed: O(k log k) - where k is the total number of tweets to sort for recent ones
# - follow/unfollow: O(1) - set operations are O(1)
# Space Complexity: O(n) - where n is the total number of tweets and relationships

# Test the Twitter class
twitter = Twitter()
twitter.postTweet(1, 5)
print(twitter.getNewsFeed(1))  # Output: [5]
twitter.follow(1, 2)
twitter.postTweet(2, 6)
print(twitter.getNewsFeed(1))  # Output: [6, 5]
twitter.unfollow(1, 2)
print(twitter.getNewsFeed(1))  # Output: [5]
```

---

### Problem 7: Find Median from Data Stream

#### Problem Understanding:

- **Problem Explanation**: The task is to design a data structure that supports the following operations efficiently:
  - `addNum(num)`: Adds a number to the data stream.
  - `findMedian()`: Returns the median of all elements so far.

**Example**:

```
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);  
medianFinder.addNum(2);  
medianFinder.findMedian(); // returns 1.5
medianFinder.addNum(3);  
medianFinder.findMedian(); // returns 2
```

#### Coding Pattern:

- This problem can be solved using two **Heaps**:
  - A max-heap to store the smaller half of the numbers.
  - A min-heap to store the larger half.

#### Solution:

```python
import heapq

class MedianFinder:

    def __init__(self):
        # Max-heap to store the smaller half of the numbers (inverted for max-heap)
        self.small = []
        # Min-heap to store the larger half of the numbers
        self.large = []

    def addNum(self, num: int) -> None:
        # Step 1: Add the number to the small heap (max-heap)
        heapq.heappush(self.small, -num)
      
        # Step 2: Balance the heaps (ensure elements in small are <= elements in large)
        if self.small and self.large and (-self.small[0] > self.large[0]):
            heapq.heappush(self.large, -heapq.heappop(self.small))
      
        # Step 3: Maintain the size property (either equal or small has one more element)
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        # If the heaps are of different sizes, return the middle element from the larger heap
        if len(self.small) > len(self.large):
            return -self.small[0]
        # If the heaps are the same size, return the average of the two middle elements
        return (-self.small[0] + self.large[0]) / 2

# Time Complexity: 
# - addNum: O(log n) for heap insertion and balancing
# - findMedian: O(1) for retrieving the median
# Space Complexity: O(n) - for storing the elements in two heaps

# Test the MedianFinder class
medianFinder = MedianFinder()
medianFinder.addNum(1)
medianFinder.addNum(2)
print(medianFinder.findMedian())  # Output: 1.5
medianFinder.addNum(

3)
print(medianFinder.findMedian())  # Output: 2
```

---

## Backtracking Section

### Problem 1: Subsets

#### Problem Understanding:

- **Problem Explanation**: Given an integer array `nums` of unique elements, return all possible subsets (the power set). The solution set must not contain duplicate subsets.

**Example**:
Input: `nums = [1, 2, 3]`
Output: `[[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]`

#### Coding Pattern:

- This problem can be solved using **Backtracking** by exploring all possible subsets recursively.

#### Solution:

```python
def subsets(nums):
    result = []  # To store all the subsets

    def backtrack(start, current_subset):
        # Append the current subset (make a copy to avoid mutation issues)
        result.append(current_subset[:])
      
        # Explore all other subsets by adding more elements
        for i in range(start, len(nums)):
            # Include nums[i] in the current subset
            current_subset.append(nums[i])
            # Recur with the next elements
            backtrack(i + 1, current_subset)
            # Backtrack: remove the last element to try other combinations
            current_subset.pop()

    # Start the backtracking with an empty subset
    backtrack(0, [])
    return result

# Time Complexity: O(2^n) - where n is the number of elements, each element can be included/excluded
# Space Complexity: O(n) - for the recursion stack

# Test the function with the example
print(subsets([1, 2, 3]))  # Output: [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
```

---

### Problem 2: Combination Sum

#### Problem Understanding:

- **Problem Explanation**: Given an array of distinct integers `candidates` and a target integer `target`, return all unique combinations of `candidates` where the chosen numbers sum to `target`. You may use each number in the candidates array multiple times.

**Example**:
Input: `candidates = [2, 3, 6, 7]`, `target = 7`
Output: `[[2, 2, 3], [7]]`

#### Coding Pattern:

- This problem can be solved using **Backtracking** to explore all possible combinations, allowing repetition of elements.

#### Solution:

```python
def combination_sum(candidates, target):
    result = []  # To store all valid combinations

    def backtrack(remaining, start, current_combination):
        # If the remaining sum is zero, add the current combination
        if remaining == 0:
            result.append(current_combination[:])
            return
      
        # If the remaining sum is negative, stop exploring further
        if remaining < 0:
            return
      
        # Explore each candidate from the current starting point
        for i in range(start, len(candidates)):
            current_combination.append(candidates[i])  # Include candidates[i] in the combination
            # Recur with the updated remaining sum (we can reuse candidates[i])
            backtrack(remaining - candidates[i], i, current_combination)
            current_combination.pop()  # Backtrack and remove the last element

    # Start the backtracking with the target sum and empty combination
    backtrack(target, 0, [])
    return result

# Time Complexity: O(2^n) - where n is the number of candidates, as we explore combinations recursively
# Space Complexity: O(n) - for the recursion stack

# Test the function with the example
print(combination_sum([2, 3, 6, 7], 7))  # Output: [[2, 2, 3], [7]]
```

---

### Problem 3: Permutations

#### Problem Understanding:

- **Problem Explanation**: Given an array `nums` of distinct integers, return all possible permutations.

**Example**:
Input: `nums = [1, 2, 3]`
Output: `[[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]`

#### Coding Pattern:

- This problem can be solved using **Backtracking** by exploring all possible ways to arrange the elements in the array.

#### Solution:

```python
def permute(nums):
    result = []  # To store all permutations

    def backtrack(current_permutation):
        # If the current permutation is complete, add it to the result
        if len(current_permutation) == len(nums):
            result.append(current_permutation[:])
            return
      
        # Try each element in the array
        for num in nums:
            if num in current_permutation:
                continue  # Skip if num is already used in the permutation
            current_permutation.append(num)  # Include num in the permutation
            backtrack(current_permutation)  # Recur with the next step
            current_permutation.pop()  # Backtrack by removing the last element

    # Start the backtracking with an empty permutation
    backtrack([])
    return result

# Time Complexity: O(n * n!) - there are n! permutations, and each permutation takes O(n) to build
# Space Complexity: O(n) - for the recursion stack

# Test the function with the example
print(permute([1, 2, 3]))  # Output: [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
```

---

### Problem 4: Subsets II

#### Problem Understanding:

- **Problem Explanation**: Given an integer array `nums` that may contain duplicates, return all possible subsets (the power set). The solution set must not contain duplicate subsets.

**Example**:
Input: `nums = [1, 2, 2]`
Output: `[[], [1], [2], [1, 2], [2, 2], [1, 2, 2]]`

#### Coding Pattern:

- This problem can be solved using **Backtracking**. To handle duplicates, we must sort the array and skip elements that are the same as the previous one.

#### Solution:

```python
def subsets_with_dup(nums):
    result = []  # To store all unique subsets
    nums.sort()  # Sort the array to handle duplicates

    def backtrack(start, current_subset):
        # Append the current subset
        result.append(current_subset[:])
      
        # Explore all other subsets by adding more elements
        for i in range(start, len(nums)):
            # Skip duplicates (only consider the first occurrence of each element)
            if i > start and nums[i] == nums[i - 1]:
                continue
            current_subset.append(nums[i])  # Include nums[i] in the current subset
            backtrack(i + 1, current_subset)  # Recur with the next elements
            current_subset.pop()  # Backtrack and remove the last element

    # Start the backtracking with an empty subset
    backtrack(0, [])
    return result

# Time Complexity: O(2^n) - where n is the number of elements (each element can be included/excluded)
# Space Complexity: O(n) - for the recursion stack

# Test the function with the example
print(subsets_with_dup([1, 2, 2]))  # Output: [[], [1], [2], [1, 2], [2, 2], [1, 2, 2]]
```

---

### Problem 5: Combination Sum II

#### Problem Understanding:

- **Problem Explanation**: Given a collection of candidate numbers `candidates` and a target number `target`, return all unique combinations where the candidate numbers sum to `target`. Each number in `candidates` may only be used once.

**Example**:
Input: `candidates = [10,1,2,7,6,1,5]`, `target = 8`
Output: `[[1,1,6], [1,2,5], [1,7], [2,6]]`

#### Coding Pattern:

- This problem can be solved using **Backtracking**. To handle duplicates, we must sort the array and skip over duplicate elements after exploring them.

#### Solution:

```python
def combination_sum2(candidates, target):
    result = []  # To store all unique combinations
    candidates.sort()  # Sort the candidates to handle duplicates

    def backtrack(remaining, start, current_combination):
        # If the remaining sum is zero, add the current combination
        if remaining == 0:
            result.append(current_combination[:])
            return
      
        # Explore each candidate from the current starting point
        for i in range(start, len(candidates)):
            # Skip duplicates (only consider the first occurrence of each element)
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            if candidates[i] > remaining:
                break  # Stop if the current number is greater than the remaining sum
            current_combination.append(candidates[i])  # Include candidates[i] in the combination
            backtrack(remaining - candidates[i], i + 1, current_combination)  # Recur with the next elements
            current_comb

ination.pop()  # Backtrack and remove the last element

    # Start the backtracking with the target sum and an empty combination
    backtrack(target, 0, [])
    return result

# Time Complexity: O(2^n) - as we explore combinations recursively
# Space Complexity: O(n) - for the recursion stack

# Test the function with the example
print(combination_sum2([10, 1, 2, 7, 6, 1, 5], 8))  # Output: [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
```

---

### Problem 6: Word Search

#### Problem Understanding:

- **Problem Explanation**: Given an `m x n` board and a word, find if the word exists in the grid. The word can be constructed from letters of sequentially adjacent cells, where "adjacent" cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

**Example**:
Input: `board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]`, `word = "ABCCED"`
Output: `True`

#### Coding Pattern:

- This problem can be solved using **Backtracking** to explore all potential paths starting from each cell on the board.

#### Solution:

```python
def exist(board, word):
    rows, cols = len(board), len(board[0])  # Get the dimensions of the board
  
    def backtrack(r, c, idx):
        # Base case: if we have found the entire word, return True
        if idx == len(word):
            return True
      
        # Check the boundaries and if the current letter matches the word[idx]
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[idx]:
            return False
      
        # Temporarily mark the cell as visited
        temp, board[r][c] = board[r][c], '#'
      
        # Explore all four directions (up, down, left, right)
        found = (backtrack(r + 1, c, idx + 1) or
                 backtrack(r - 1, c, idx + 1) or
                 backtrack(r, c + 1, idx + 1) or
                 backtrack(r, c - 1, idx + 1))
      
        # Backtrack: restore the original value in the board
        board[r][c] = temp
      
        return found

    # Try starting from every cell on the board
    for r in range(rows):
        for c in range(cols):
            if backtrack(r, c, 0):  # Start backtracking with the first letter of the word
                return True
  
    return False

# Time Complexity: O(m * n * 4^l) - where m * n is the size of the board, and l is the length of the word
# Space Complexity: O(l) - for the recursion stack (l is the length of the word)

# Test the function with the example
print(exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"))  # Output: True
```

#### Alternative Approach:

- **No alternative approach**. Backtracking is the most suitable solution for this type of problem where multiple paths need to be explored.

---

### Problem 7: Palindrome Partitioning

#### Problem Understanding:

- **Problem Explanation**: Given a string `s`, partition `s` such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of `s`.

**Example**:
Input: `s = "aab"`
Output: `[["a","a","b"],["aa","b"]]`

#### Coding Pattern:

- This problem can be solved using **Backtracking** to explore all possible ways to partition the string.

#### Solution:

```python
def partition(s):
    result = []  # To store all the partitions

    def backtrack(start, current_partition):
        # If we have partitioned the entire string, add the current partition to the result
        if start == len(s):
            result.append(current_partition[:])
            return
      
        # Try to partition the string at every possible position
        for end in range(start + 1, len(s) + 1):
            # If the substring s[start:end] is a palindrome, explore further
            if s[start:end] == s[start:end][::-1]:
                current_partition.append(s[start:end])
                backtrack(end, current_partition)  # Recur for the next part of the string
                current_partition.pop()  # Backtrack to try other partitions

    # Start the backtracking with the entire string
    backtrack(0, [])
    return result

# Time Complexity: O(2^n) - since we explore every possible partition of the string
# Space Complexity: O(n) - for the recursion stack

# Test the function with the example
print(partition("aab"))  # Output: [["a","a","b"],["aa","b"]]
```

#### Alternative Approach:

- **No alternative approach**. Backtracking is the optimal approach to explore all palindrome partitions efficiently.

---

### Problem 8: Letter Combinations of a Phone Number

#### Problem Understanding:

- **Problem Explanation**: Given a string containing digits from `2-9` inclusive, return all possible letter combinations that the number could represent. A mapping of digit to letters (just like on the telephone buttons) is given below:
  - 2 -> "abc"
  - 3 -> "def"
  - 4 -> "ghi"
  - 5 -> "jkl"
  - 6 -> "mno"
  - 7 -> "pqrs"
  - 8 -> "tuv"
  - 9 -> "wxyz"

**Example**:
Input: `digits = "23"`
Output: `["ad","ae","af","bd","be","bf","cd","ce","cf"]`

#### Coding Pattern:

- This problem can be solved using **Backtracking** to explore all possible combinations of letters.

#### Solution:

```python
def letter_combinations(digits):
    if not digits:
        return []
  
    # Mapping of digits to corresponding letters
    phone_map = {
        "2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
        "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
    }
  
    result = []  # To store all letter combinations

    def backtrack(index, current_combination):
        # If the combination is complete (equal to the length of digits), add it to the result
        if index == len(digits):
            result.append("".join(current_combination))
            return
      
        # Get the letters that the current digit can represent
        letters = phone_map[digits[index]]
        # Explore each letter as part of the combination
        for letter in letters:
            current_combination.append(letter)
            backtrack(index + 1, current_combination)  # Move to the next digit
            current_combination.pop()  # Backtrack and try another letter

    # Start the backtracking with the first digit
    backtrack(0, [])
    return result

# Time Complexity: O(4^n) - where n is the length of digits (each digit can have up to 4 letters)
# Space Complexity: O(n) - for the recursion stack

# Test the function with the example
print(letter_combinations("23"))  # Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
```

#### Alternative Approach:

- **No alternative approach**. Backtracking is the most suitable method to generate all combinations of letters for a given sequence of digits.

---

### Problem 9: N-Queens

#### Problem Understanding:

- **Problem Explanation**: The N-Queens problem is the problem of placing `n` chess queens on an `n x n` chessboard so that no two queens attack each other. Return all distinct solutions to the N-Queens puzzle.

**Example**:
Input: `n = 4`
Output:

```
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],
  
 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
```

#### Coding Pattern:

- This problem can be solved using **Backtracking** to explore all possible configurations and validate whether each configuration is a valid solution.

#### Solution:

```python
def solve_n_queens(n):
    result = []  # To store all valid solutions
    board = [["."] * n for _ in range(n)]  # Initialize an empty board
  
    # Helper function to check if placing a queen at (row, col) is valid
    def is_valid(row, col):
        # Check column
        for r in range(row):
            if board[r][col] == "Q":
                return False
        # Check diagonal (top-left to bottom-right)
        for r, c in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
            if board[r][c] == "Q":
                return False
        # Check diagonal (top-right to bottom-left)
        for r, c in zip(range(row - 1, -1, -1), range(col + 1, n)):
            if board[r][c] == "Q":
                return False
        return True
  
    # Backtracking function to place queens row by row
    def backtrack(row):
        if row == n:
            # Convert the board to a valid solution format and append it
            result.append(["".

join(r) for r in board])
            return
      
        # Try placing a queen in each column of the current row
        for col in range(n):
            if is_valid(row, col):
                board[row][col] = "Q"  # Place the queen
                backtrack(row + 1)  # Recur to place queens in the next row
                board[row][col] = "."  # Backtrack and remove the queen
  
    # Start backtracking from the first row
    backtrack(0)
    return result

# Time Complexity: O(n!) - for exploring all possible placements of queens
# Space Complexity: O(n) - for the recursion stack and storing the board

# Test the function with the example
print(solve_n_queens(4))
```

#### Alternative Approach:

- **No alternative approach**. Backtracking is the most efficient way to solve the N-Queens problem by exploring all possible placements of queens and pruning invalid configurations early.

---

## Tries Section

### Problem 1: Implement Trie (Prefix Tree)

#### Problem Understanding:

- **Problem Explanation**: A trie (pronounced as "try") or prefix tree is a data structure used to efficiently store and search strings, typically words. Implement a `Trie` class with the following functions:
  - `insert(word)`: Inserts a word into the trie.
  - `search(word)`: Returns `True` if the word is in the trie (i.e., was inserted before), `False` otherwise.
  - `startsWith(prefix)`: Returns `True` if there is any word in the trie that starts with the given prefix, `False` otherwise.

**Example**:

```
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // returns True
trie.search("app");     // returns False
trie.startsWith("app"); // returns True
trie.insert("app");
trie.search("app");     // returns True
```

#### Coding Pattern:

- This problem can be solved by constructing a **Trie** (prefix tree) where each node stores its children and a flag indicating if a word ends at that node.

#### Solution:

```python
class TrieNode:
    def __init__(self):
        # Dictionary to store children nodes (a-z)
        self.children = {}
        # Flag to indicate the end of a word
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        # Initialize the root node
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # Start from the root node
        node = self.root
        # Traverse through each character in the word
        for char in word:
            # If the character is not a child of the current node, create a new node
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]  # Move to the child node
        # Mark the end of the word
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        # Start from the root node
        node = self.root
        # Traverse through each character in the word
        for char in word:
            if char not in node.children:
                return False  # If character is not found, word does not exist
            node = node.children[char]  # Move to the next node
        # Check if this is the end of a word
        return node.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        # Start from the root node
        node = self.root
        # Traverse through each character in the prefix
        for char in prefix:
            if char not in node.children:
                return False  # If character is not found, no word with this prefix
            node = node.children[char]  # Move to the next node
        return True  # Prefix exists

# Time Complexity: O(n) - where n is the length of the word/prefix for both insert and search operations
# Space Complexity: O(n) - for storing n characters in the Trie for each word

# Test the Trie class with the example
trie = Trie()
trie.insert("apple")
print(trie.search("apple"))   # Output: True
print(trie.search("app"))     # Output: False
print(trie.startsWith("app")) # Output: True
trie.insert("app")
print(trie.search("app"))     # Output: True
```

#### Alternative Approach:

- **No alternative approach**. A Trie (prefix tree) is the most efficient data structure for problems involving prefix searches and insertions.

---

### Problem 2: Design Add and Search Words Data Structure

#### Problem Understanding:

- **Problem Explanation**: Design a data structure that supports adding new words and finding if a string matches any previously added string. A string could contain the dot character `'.'` to represent any one letter. Implement the `WordDictionary` class:
  - `addWord(word)`: Adds `word` to the data structure.
  - `search(word)`: Returns `True` if the word or pattern (containing `.`) is found, otherwise `False`.

**Example**:

```
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // returns False
wordDictionary.search("bad"); // returns True
wordDictionary.search(".ad"); // returns True
wordDictionary.search("b.."); // returns True
```

#### Coding Pattern:

- This problem can be solved by modifying a **Trie** to handle the wildcard character `.` during the search operation.

#### Solution:

```python
class WordDictionary:
    def __init__(self):
        # Trie node with children and end-of-word marker
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        # Insert the word into the trie
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True  # Mark the end of the word

    def search(self, word: str) -> bool:
        # Helper function to search with support for '.'
        def dfs(j, node):
            # Perform depth-first search
            for i in range(j, len(word)):
                char = word[i]
                if char == '.':
                    # If current character is '.', try all possible paths
                    for child in node.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if char not in node.children:
                        return False
                    node = node.children[char]
            return node.is_end_of_word
      
        # Start the search from the root
        return dfs(0, self.root)

# Time Complexity: O(n) - for adding words, and O(n * 26^k) for searching with the '.' wildcard (where k is the length of the word)
# Space Complexity: O(n) - for storing n characters in the Trie

# Test the WordDictionary class with the example
wordDictionary = WordDictionary()
wordDictionary.addWord("bad")
wordDictionary.addWord("dad")
wordDictionary.addWord("mad")
print(wordDictionary.search("pad"))  # Output: False
print(wordDictionary.search("bad"))  # Output: True
print(wordDictionary.search(".ad"))  # Output: True
print(wordDictionary.search("b.."))  # Output: True
```

#### Alternative Approach:

- **No alternative approach**. Using a Trie with recursive backtracking for handling the wildcard character `.` is the most effective solution for this problem.

---

### Problem 3: Word Search II

#### Problem Understanding:

- **Problem Explanation**: Given an `m x n` board of characters and a list of strings `words`, find all the words on the board. The word can be constructed from letters of sequentially adjacent cells, where "adjacent" cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

**Example**:
Input: `board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]`, `words = ["oath","pea","eat","rain"]`
Output: `["eat","oath"]`

#### Coding Pattern:

- This problem can be solved using **Trie** (prefix tree) combined with **Backtracking** to explore the board and search for words.

#### Solution:

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.word = None  # Store the complete word at the end node

class WordSearchTrie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # Insert the word into the trie
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        node.word = word  # Store the complete word

class Solution:
    def findWords(self, board, words):
        # Build a trie of the words
        trie = WordSearchTrie()
        for word in words:
            trie.insert(word)
      
        rows, cols = len(board), len(board[0])
        result = set()  # Use a set to avoid duplicate words

        def backtrack(r, c, node):
            # Base case: if we reach a cell with no corresponding trie node, return
            char = board[r][c]
            if char not in node.children:
                return
            # Move to the next trie node
            node = node.children[char]
            if node.is_end_of_word:
                result.add(node.word)  # Add the word to the result
          
            # Mark the cell as visited by temporarily changing its value
            board[r][c] = '#'
          
            # Explore neighbors (up, down, left, right)
            for dr, dc in [(-1, 0), (1, 0), (0

, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != '#':
                    backtrack(nr, nc, node)
          
            # Backtrack: restore the original value in the board
            board[r][c] = char
      
        # Start backtracking from each cell
        for r in range(rows):
            for c in range(cols):
                backtrack(r, c, trie.root)
      
        return list(result)

# Time Complexity: O(m * n * 4^l) - where m*n is the size of the board and l is the maximum length of the word
# Space Complexity: O(k) - where k is the total number of letters in the Trie

# Test the function with the example
board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath", "pea", "eat", "rain"]
solution = Solution()
print(solution.findWords(board, words))  # Output: ["eat", "oath"]
```

#### Alternative Approach:

- **No alternative approach**. Using a Trie with backtracking is the most effective way to solve this problem, efficiently combining word search with prefix-based optimizations.

---

## Graphs Section

### Problem 1: Number of Islands

#### Problem Understanding:

- **Problem Explanation**: Given an `m x n` 2D grid of '1's (land) and '0's (water), return the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are surrounded by water.

**Example**:
Input:

```
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
```

Output: `3`

#### Coding Pattern:

- This problem can be solved using **Depth-First Search (DFS)** to traverse each island and mark its area as visited.

#### Solution:

```python
def num_islands(grid):
    if not grid:
        return 0
  
    rows, cols = len(grid), len(grid[0])
    num_of_islands = 0

    def dfs(r, c):
        # Base case: stop if out of bounds or at water ('0')
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
            return
      
        # Mark the current cell as visited (change '1' to '0')
        grid[r][c] = '0'
      
        # Explore the neighbors in all four directions (up, down, left, right)
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    # Iterate through the grid and apply DFS whenever we find land ('1')
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':  # Found an unvisited island
                num_of_islands += 1  # Increment the island count
                dfs(r, c)  # Perform DFS to mark the entire island

    return num_of_islands

# Time Complexity: O(m * n) - where m is the number of rows and n is the number of columns in the grid
# Space Complexity: O(m * n) - due to the recursion stack and the grid size

# Test the function with the example
grid = [
  ["1", "1", "0", "0", "0"],
  ["1", "1", "0", "0", "0"],
  ["0", "0", "1", "0", "0"],
  ["0", "0", "0", "1", "1"]
]
print(num_islands(grid))  # Output: 3
```

#### Alternative Approach:

- **Breadth-First Search (BFS)** can also be used to solve this problem. Instead of recursively exploring the island with DFS, we can use a queue to iteratively explore the land.

  Here's the BFS alternative approach:

```python
from collections import deque

def num_islands_bfs(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    num_of_islands = 0

    def bfs(r, c):
        queue = deque([(r, c)])
        grid[r][c] = '0'  # Mark as visited
        while queue:
            r, c = queue.popleft()
            # Explore all four directions
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                    queue.append((nr, nc))
                    grid[nr][nc] = '0'  # Mark as visited

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':  # Found an unvisited island
                num_of_islands += 1
                bfs(r, c)  # Perform BFS to mark the entire island

    return num_of_islands

# Time Complexity: O(m * n) - same as DFS
# Space Complexity: O(min(m, n)) - for the queue used in BFS

# Test the BFS function
print(num_islands_bfs([
  ["1", "1", "0", "0", "0"],
  ["1", "1", "0", "0", "0"],
  ["0", "0", "1", "0", "0"],
  ["0", "0", "0", "1", "1"]
]))  # Output: 3
```

---

### Problem 2: Max Area of Island

#### Problem Understanding:

- **Problem Explanation**: You are given an `m x n` binary matrix `grid` where '1' represents land and '0' represents water. Return the maximum area of an island in `grid`. An island is a group of connected '1's (land) connected vertically or horizontally. You may assume all four edges of the grid are surrounded by water.

**Example**:
Input:

```
grid = [
  [0,0,1,0,0,0,0,1,0,0,0,0,0],
  [0,0,0,0,0,0,0,1,1,1,0,0,0],
  [0,1,1,0,1,0,0,0,0,0,0,0,0],
  [0,1,0,0,1,1,0,0,1,0,1,0,0],
  [0,1,0,0,1,1,0,0,1,1,1,0,0],
  [0,0,0,0,0,0,0,0,0,0,1,0,0],
  [0,0,0,0,0,0,0,1,1,1,0,0,0],
  [0,0,0,0,0,0,0,1,1,0,0,0,0]
]
```

Output: `6`

#### Coding Pattern:

- This problem can be solved using **Depth-First Search (DFS)** to explore the island area recursively and count its size.

#### Solution:

```python
def max_area_of_island(grid):
    if not grid:
        return 0
  
    rows, cols = len(grid), len(grid[0])
    max_area = 0

    def dfs(r, c):
        # Base case: stop if out of bounds or at water ('0')
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
            return 0
      
        # Mark the current cell as visited (change '1' to '0') and initialize area to 1
        grid[r][c] = '0'
        area = 1  # Count the current cell
      
        # Explore all four directions and accumulate the area
        area += dfs(r + 1, c)
        area += dfs(r - 1, c)
        area += dfs(r, c + 1)
        area += dfs(r, c - 1)
      
        return area

    # Iterate through the grid and apply DFS whenever we find land ('1')
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':  # Found an unvisited land cell
                max_area = max(max_area, dfs(r, c))  # Update the maximum area

    return max_area

# Time Complexity: O(m * n) - where m is the number of rows and n is the number of columns in the grid
# Space Complexity: O(m * n) - due to the recursion stack and the grid size

# Test the function with the example
grid = [
  [0,0,1,0,0,0,0,1,0,0,0,0,0],
  [0,0,0,0,0,0,0,1,1,1,0,0,0],
  [0,1,1,0,1,0,0,0,0,0,0,0,0],
  [0,1,0,0,1,1,0,0,1,0,1,0,0],
  [0,1,0,0,1,1,0,0,1,1,1,0,0],
  [0,0,0,0,0,0,0,0,0,0,1,0,0],
  [0,0,0,0,0,0,0,1,1,1,0,0,0],
  [0,0,0,0,0,0,0,1,1,0,0,0,0]
]
print(max_area_of_island(grid))  # Output: 6
```

#### Alternative Approach:

- **Breadth-First Search (BFS)** can also be used to explore the island iteratively. This would replace the recursive DFS with an

 iterative queue-based BFS approach to calculate the area of each island.

  Here's the BFS alternative approach:

```python
from collections import deque

def max_area_of_island_bfs(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    max_area = 0

    def bfs(r, c):
        queue = deque([(r, c)])
        grid[r][c] = '0'  # Mark as visited
        area = 1  # Count the current cell
        while queue:
            r, c = queue.popleft()
            # Explore all four directions
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                    queue.append((nr, nc))
                    grid[nr][nc] = '0'  # Mark as visited
                    area += 1
        return area

    # Iterate through the grid and apply BFS whenever we find land ('1')
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                max_area = max(max_area, bfs(r, c))  # Update the maximum area

    return max_area

# Test the BFS function
print(max_area_of_island_bfs([
  [0,0,1,0,0,0,0,1,0,0,0,0,0],
  [0,0,0,0,0,0,0,1,1,1,0,0,0],
  [0,1,1,0,1,0,0,0,0,0,0,0,0],
  [0,1,0,0,1,1,0,0,1,0,1,0,0],
  [0,1,0,0,1,1,0,0,1,1,1,0,0],
  [0,0,0,0,0,0,0,0,0,0,1,0,0],
  [0,0,0,0,0,0,0,1,1,1,0,0,0],
  [0,0,0,0,0,0,0,1,1,0,0,0,0]
]))  # Output: 6
```

---

### Problem 3: Clone Graph

#### Problem Understanding:

- **Problem Explanation**: Given a reference of a node in a **connected** undirected graph, return a deep copy (clone) of the graph. Each node in the graph contains a value (`val`) and a list (`neighbors`) of its neighbors.

**Example**:
Input:

```
1 -- 2
|    |
4 -- 3
```

Output: A deep clone of this graph.

#### Coding Pattern:

- This problem can be solved using either **Depth-First Search (DFS)** or **Breadth-First Search (BFS)** to traverse the graph and copy each node and its neighbors.

#### Solution (DFS):

```python
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def clone_graph(node: 'Node') -> 'Node':
    if not node:
        return None
  
    # Dictionary to store the mapping from original node to the cloned node
    cloned_nodes = {}

    def dfs(current_node):
        # If the node is already cloned, return the cloned node
        if current_node in cloned_nodes:
            return cloned_nodes[current_node]
      
        # Create a new clone for the current node
        clone = Node(current_node.val)
        cloned_nodes[current_node] = clone
      
        # Recursively clone all the neighbors
        for neighbor in current_node.neighbors:
            clone.neighbors.append(dfs(neighbor))
      
        return clone
  
    # Start DFS traversal and clone the graph
    return dfs(node)

# Time Complexity: O(n) - where n is the number of nodes in the graph (we visit each node once)
# Space Complexity: O(n) - for storing the cloned nodes and the recursion stack

# Test the function with a small graph (manually create the graph and test cloning)
```

#### Alternative Approach:

- **BFS (Breadth-First Search)** can also be used to clone the graph iteratively. Instead of recursively traversing the graph, BFS uses a queue to process each node level by level.

Here's the BFS alternative approach:

```python
from collections import deque

def clone_graph_bfs(node: 'Node') -> 'Node':
    if not node:
        return None
  
    # Dictionary to store the mapping from original node to the cloned node
    cloned_nodes = {}
    # Queue to process nodes in BFS manner
    queue = deque([node])
  
    # Clone the root node
    cloned_nodes[node] = Node(node.val)
  
    # Start BFS traversal
    while queue:
        current_node = queue.popleft()
      
        # Iterate over the neighbors of the current node
        for neighbor in current_node.neighbors:
            if neighbor not in cloned_nodes:
                # Clone the neighbor if it hasn't been cloned yet
                cloned_nodes[neighbor] = Node(neighbor.val)
                queue.append(neighbor)
          
            # Link the clone of the current node to the clone of the neighbor
            cloned_nodes[current_node].neighbors.append(cloned_nodes[neighbor])
  
    return cloned_nodes[node]

# Time Complexity: O(n) - where n is the number of nodes in the graph
# Space Complexity: O(n) - for storing the cloned nodes and the queue

# Test the BFS function with a small graph (manually create the graph and test cloning)
```

---

### Problem 4: Walls and Gates

#### Problem Understanding:

- **Problem Explanation**: You are given a grid `rooms` where:
  - `-1` represents a wall or obstacle.
  - `0` represents a gate.
  - `∞` represents an empty room.

Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, leave the distance as `∞`.

**Example**:
Input:

```
rooms = [
  [∞, -1, 0, ∞],
  [∞, ∞, ∞, -1],
  [∞, -1, ∞, -1],
  [0, -1, ∞, ∞]
]
```

Output:

```
[
  [3, -1, 0, 1],
  [2, 2, 1, -1],
  [1, -1, 2, -1],
  [0, -1, 3, 4]
]
```

#### Coding Pattern:

- This problem can be solved using **Breadth-First Search (BFS)** starting from each gate (i.e., nodes with value `0`). BFS ensures that we find the shortest path from a gate to each empty room.

#### Solution:

```python
from collections import deque

def walls_and_gates(rooms):
    if not rooms:
        return
  
    rows, cols = len(rooms), len(rooms[0])
    queue = deque()

    # Enqueue all gates (cells with value 0)
    for r in range(rows):
        for c in range(cols):
            if rooms[r][c] == 0:
                queue.append((r, c))

    # BFS from all gates at once
    while queue:
        r, c = queue.popleft()
      
        # Explore all four directions (up, down, left, right)
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r + dr, c + dc
            # If the new position is within bounds and is an empty room (∞)
            if 0 <= nr < rows and 0 <= nc < cols and rooms[nr][nc] == float('inf'):
                # Update the distance and add the new position to the queue
                rooms[nr][nc] = rooms[r][c] + 1
                queue.append((nr, nc))

# Time Complexity: O(m * n) - where m is the number of rows and n is the number of columns
# Space Complexity: O(m * n) - for storing the queue

# Test the function with the example grid
rooms = [
  [float('inf'), -1, 0, float('inf')],
  [float('inf'), float('inf'), float('inf'), -1],
  [float('inf'), -1, float('inf'), -1],
  [0, -1, float('inf'), float('inf')]
]
walls_and_gates(rooms)
print(rooms)  # Output: [[3, -1, 0, 1], [2, 2, 1, -1], [1, -1, 2, -1], [0, -1, 3, 4]]
```

#### Alternative Approach:

- **No alternative approach**. BFS is the most suitable solution for this problem as it guarantees that the shortest distance from each gate to an empty room is computed efficiently.

---

### Problem 5: Rotting Oranges

#### Problem Understanding:

- **Problem Explanation**: You are given an `m x n` grid where each cell can have one of three values:
  - `0` representing an empty cell.
  - `1` representing a fresh orange.
  - `2` representing a rotten orange.

Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten. Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return `-1`.

**Example**:
Input:

```
grid = [
  [2,1,1],
  [1,1,0],
  [0,1,1]
]
```

Output: `4`

#### Coding Pattern:

- This problem can be solved using **Breadth-First Search (BFS)** to propagate the rot from all initially rotten oranges to adjacent fresh ones, keeping track of the time.

#### Solution:

```python
from collections import deque

def oranges_rotting(grid):
    if not grid:
        return -1
  
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh_oranges = 0
  
    # Initialize the queue with all rotten oranges and count fresh oranges
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c))  # Add rotten oranges to the queue
            elif grid[r][c] == 1:
                fresh_oranges += 1  # Count fresh oranges
  
    if fresh_oranges == 0:
        return 0  # No fresh oranges to rot, return 0
  
    # BFS to rot adjacent oranges
    minutes_passed = 0
    while queue:
        minutes_passed += 1
        for _ in range(len(queue)):
            r, c = queue.popleft()
          
            # Explore all four directions (up, down, left, right)
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2  # Rot the fresh orange
                    fresh_oranges -= 1  # Decrease the count of fresh oranges
                    queue.append((nr, nc))  # Add

 the newly rotten orange to the queue
  
    # If there are still fresh oranges left, return -1, otherwise return minutes_passed
    return minutes_passed - 1 if fresh_oranges == 0 else -1

# Time Complexity: O(m * n) - where m is the number of rows and n is the number of columns
# Space Complexity: O(m * n) - for storing the queue

# Test the function with the example grid
grid = [
  [2, 1, 1],
  [1, 1, 0],
  [0, 1, 1]
]
print(oranges_rotting(grid))  # Output: 4
```

#### Alternative Approach:

- **No alternative approach**. BFS is the most efficient way to propagate the rotting process and track the time taken.

---

### Problem 6: Pacific Atlantic Water Flow

#### Problem Understanding:

- **Problem Explanation**: Given an `m x n` matrix of non-negative integers representing the height of each cell, find the list of grid coordinates where water can flow to both the Pacific and Atlantic oceans. Water can only flow in four directions (up, down, left, right) and can flow from a cell to another one with a height equal or lower.

**Example**:
Input:

```
matrix = [
  [1,2,2,3,5],
  [3,2,3,4,4],
  [2,4,5,3,1],
  [6,7,1,4,5],
  [5,1,1,2,4]
]
```

Output:

```
[[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
```

#### Coding Pattern:

- This problem can be solved using **Depth-First Search (DFS)** starting from both the Pacific and Atlantic edges to explore the cells where water can flow. The cells visited by both DFS traversals are the ones where water can flow to both oceans.

#### Solution:

```python
def pacific_atlantic(matrix):
    if not matrix:
        return []
  
    rows, cols = len(matrix), len(matrix[0])
    pacific_reachable = set()  # Cells reachable by the Pacific
    atlantic_reachable = set()  # Cells reachable by the Atlantic

    def dfs(r, c, visited, prev_height):
        # Base case: if out of bounds or if the current cell is lower than the previous one
        if (r, c) in visited or r < 0 or r >= rows or c < 0 or c >= cols or matrix[r][c] < prev_height:
            return
        visited.add((r, c))  # Mark the current cell as visited
        # Explore all four directions
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            dfs(r + dr, c + dc, visited, matrix[r][c])

    # Start DFS from the Pacific ocean (top and left edges)
    for r in range(rows):
        dfs(r, 0, pacific_reachable, matrix[r][0])
        dfs(r, cols - 1, atlantic_reachable, matrix[r][cols - 1])
  
    for c in range(cols):
        dfs(0, c, pacific_reachable, matrix[0][c])
        dfs(rows - 1, c, atlantic_reachable, matrix[rows - 1][c])

    # The result is the intersection of cells reachable by both Pacific and Atlantic
    return list(pacific_reachable & atlantic_reachable)

# Time Complexity: O(m * n) - where m is the number of rows and n is the number of columns
# Space Complexity: O(m * n) - for the visited sets and recursion stack

# Test the function with the example matrix
matrix = [
  [1, 2, 2, 3, 5],
  [3, 2, 3, 4, 4],
  [2, 4, 5, 3, 1],
  [6, 7, 1, 4, 5],
  [5, 1, 1, 2, 4]
]
print(pacific_atlantic(matrix))  # Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
```

#### Alternative Approach:

- **No alternative approach**. DFS is the best solution for exploring cells where water can flow in multiple directions.

---

### Problem 7: Surrounded Regions

#### Problem Understanding:

- **Problem Explanation**: Given an `m x n` matrix board of 'X' and 'O', capture all regions surrounded by 'X'. A region is captured by flipping all 'O's into 'X's in that surrounded region.

**Example**:
Input:

```
board = [
  ["X", "X", "X", "X"],
  ["X", "O", "O", "X"],
  ["X", "X", "O", "X"],
  ["X", "O", "X", "X"]
]
```

Output:

```
[
  ["X", "X", "X", "X"],
  ["X", "X", "X", "X"],
  ["X", "X", "X", "X"],
  ["X", "O", "X", "X"]
]
```

#### Coding Pattern:

- This problem can be solved using **Depth-First Search (DFS)** or **Breadth-First Search (BFS)**. We'll first mark all the 'O's connected to the edges (which can't be surrounded), and then flip all the remaining 'O's to 'X's.

#### Solution (DFS):

```python
def solve(board):
    if not board:
        return
  
    rows, cols = len(board), len(board[0])

    # Helper function to perform DFS and mark connected 'O's as safe (not to be flipped)
    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != 'O':
            return
        board[r][c] = 'S'  # Mark the 'O' as safe
        # Explore the four directions (up, down, left, right)
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    # Step 1: Mark all 'O's on the boundary and their connected 'O's as safe
    for r in range(rows):
        dfs(r, 0)
        dfs(r, cols - 1)
    for c in range(cols):
        dfs(0, c)
        dfs(rows - 1, c)

    # Step 2: Flip all remaining 'O's to 'X', and convert 'S' back to 'O'
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 'O':
                board[r][c] = 'X'
            elif board[r][c] == 'S':
                board[r][c] = 'O'

# Time Complexity: O(m * n) - where m is the number of rows and n is the number of columns
# Space Complexity: O(m * n) - for the recursion stack in DFS

# Test the function with the example
board = [
  ["X", "X", "X", "X"],
  ["X", "O", "O", "X"],
  ["X", "X", "O", "X"],
  ["X", "O", "X", "X"]
]
solve(board)
print(board)  # Output: [["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "O", "X", "X"]]
```

#### Alternative Approach:

- **Breadth-First Search (BFS)** can also be used to mark the 'O's that should not be flipped. Instead of using recursive DFS, we can use a queue to iteratively mark the connected 'O's.

Here's the BFS alternative approach:

```python
from collections import deque

def solve_bfs(board):
    if not board:
        return

    rows, cols = len(board), len(board[0])

    # Helper function to perform BFS and mark connected 'O's as safe (not to be flipped)
    def bfs(r, c):
        queue = deque([(r, c)])
        board[r][c] = 'S'  # Mark the 'O' as safe
        while queue:
            r, c = queue.popleft()
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == 'O':
                    board[nr][nc] = 'S'  # Mark connected 'O' as safe
                    queue.append((nr, nc))

    # Step 1: Mark all 'O's on the boundary and their connected 'O's as safe
    for r in range(rows):
        bfs(r, 0)
        bfs(r, cols - 1)
    for c in range(cols):
        bfs(0, c)
        bfs(rows - 1, c)

    # Step 2: Flip all remaining 'O's to 'X', and convert 'S' back to 'O'
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 'O':
                board[r][c] = 'X'
            elif board[r][c] == 'S':
                board[r][c] = 'O'

# Test the BFS function
board = [
  ["X", "X", "X", "X"],
  ["X", "O", "O", "X"],
  ["X", "X", "O", "X"],
  ["X", "O", "X", "X"]
]
solve_bfs(board)
print(board)  # Output: [["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "O", "X", "X"]]
```

---

### Problem 8: Course Schedule

#### Problem Understanding:

- **Problem Explanation**: There are `n` courses labeled from `0` to `n-1`. Some courses may have prerequisites. Given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you must take course `bi` before course `ai`, determine if you can finish all courses.

**Example**:
Input:

```
n = 2
prerequisites = [[1, 0]]
```

Output: `True`

#### Coding Pattern:

- This problem can be solved using **Topological Sorting** with **Depth-First Search (DFS)** or **Kahn's Algorithm** (BFS). We need to check for cycles in the directed graph representing the prerequisites.

#### Solution (DFS):

```python
def can_finish(num_courses, prerequisites):
    # Build the adjacency list for the graph
    graph = {i: [] for i in range(num_courses)}
    for course, prereq in prerequisites:
        graph[prereq].append(course)

    # To track the state of each node (0 = unvisited, 1 = visiting, 2 = visited)
    visited = [0] * num_courses

    # Helper function to perform DFS and detect cycles
    def dfs(course):
        if visited[course] == 1:  # Cycle detected
            return False
        if visited[course] == 2:  # Already visited, no need to revisit
            return True

        visited[course] = 1  # Mark the node as visiting

        for neighbor in graph[course]:
            if not dfs(neighbor):
                return False
      
        visited[course] = 2  # Mark the node as fully processed
        return True

    # Perform DFS on all nodes
    for course in range(num_courses):
        if not dfs(course):
            return False  # Cycle detected

    return True  # No cycles, all courses can be completed

# Time Complexity: O(n + e) - where n is the number of courses, and e is the number of prerequisites
# Space Complexity: O(n + e) - for the graph and the visited array

# Test the function with the example
print(can_finish(2, [[1, 0]]))  # Output: True
```

#### Alternative Approach:

- **Kahn's Algorithm (BFS)** can also be used to perform topological sorting and detect cycles in the graph. This approach processes nodes in topological order using in-degrees.

Here's the BFS alternative approach:

```python
from collections import deque, defaultdict

def can_finish_bfs(num_courses, prerequisites):
    # Build the adjacency list and in-degree array
    graph = defaultdict(list)
    in_degree = [0] * num_courses
  
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1

    # Initialize the queue with all courses having 0 in-degree (no prerequisites)
    queue = deque([i for i in range(num_courses) if in_degree[i] == 0])
    courses_taken = 0

    # Process nodes in topological order
    while queue:
        course = queue.popleft()
        courses_taken += 1
        for neighbor in graph[course]:
            in_degree[neighbor] -= 1  # Reduce in-degree
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # If we've processed all courses, there are

 no cycles
    return courses_taken == num_courses

# Test the BFS function
print(can_finish_bfs(2, [[1, 0]]))  # Output: True
```

---

### Problem 9: Course Schedule II

#### Problem Understanding:

- **Problem Explanation**: There are `n` courses labeled from `0` to `n-1`. Some courses may have prerequisites. Given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you must take course `bi` before course `ai`, return the ordering of courses you should take to finish all courses. If there are multiple valid orderings, return any of them. If it is impossible to finish all courses, return an empty array.

**Example**:
Input:

```
n = 2
prerequisites = [[1, 0]]
```

Output: `[0, 1]`

#### Coding Pattern:

- This problem can be solved using **Topological Sorting** with **Depth-First Search (DFS)** or **Kahn's Algorithm** (BFS). We need to return a valid course order if there are no cycles.

#### Solution (DFS):

```python
def find_order(num_courses, prerequisites):
    # Build the adjacency list for the graph
    graph = {i: [] for i in range(num_courses)}
    for course, prereq in prerequisites:
        graph[prereq].append(course)

    visited = [0] * num_courses
    result = []
    cycle_found = [False]

    def dfs(course):
        if visited[course] == 1:  # Cycle detected
            cycle_found[0] = True
            return
        if visited[course] == 2:  # Already processed
            return

        visited[course] = 1  # Mark as visiting
        for neighbor in graph[course]:
            dfs(neighbor)
      
        visited[course] = 2  # Mark as fully processed
        result.append(course)

    # Perform DFS on all courses
    for course in range(num_courses):
        if visited[course] == 0:
            dfs(course)
        if cycle_found[0]:
            return []  # If a cycle is detected, return an empty array

    return result[::-1]  # Return the reverse of the result list

# Time Complexity: O(n + e) - where n is the number of courses, and e is the number of prerequisites
# Space Complexity: O(n + e) - for the graph and visited array

# Test the function with the example
print(find_order(2, [[1, 0]]))  # Output: [0, 1]
```

#### Alternative Approach:

- **Kahn's Algorithm (BFS)** can also be used to generate a topological order using in-degrees. Here's the BFS alternative approach:

```python
def find_order_bfs(num_courses, prerequisites):
    graph = defaultdict(list)
    in_degree = [0] * num_courses
  
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1

    queue = deque([i for i in range(num_courses) if in_degree[i] == 0])
    order = []

    while queue:
        course = queue.popleft()
        order.append(course)
        for neighbor in graph[course]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return order if len(order) == num_courses else []

# Test the BFS function
print(find_order_bfs(2, [[1, 0]]))  # Output: [0, 1]
```

---

### Problem 10: Graph Valid Tree

#### Problem Understanding:

- **Problem Explanation**: You have a graph with `n` nodes labeled from `0` to `n-1`. You are given a list of edges where `edges[i] = [ai, bi]` represents an undirected edge between node `ai` and node `bi`. Determine if these edges make up a valid tree.

**Example**:
Input:

```
n = 5
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
```

Output: `True`

#### Coding Pattern:

- A graph is a valid tree if:

  1. It is connected (all nodes are reachable).
  2. It contains no cycles.

  We can use **Depth-First Search (DFS)** or **Breadth-First Search (BFS)** to check both conditions.

#### Solution (DFS):

```python
def valid_tree(n, edges):
    if len(edges) != n - 1:
        return False  # A tree must have exactly n-1 edges
  
    # Build the adjacency list for the graph
    graph = {i: [] for i in range(n)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()

    # Helper function to perform DFS
    def dfs(node, parent):
        visited.add(node)
        # Explore all the neighbors of the current node
        for neighbor in graph[node]:
            if neighbor == parent:
                continue  # Ignore the edge leading back to the parent
            if neighbor in visited:
                return False  # Found a cycle
            if not dfs(neighbor, node):
                return False
        return True

    # Start DFS from node 0
    if not dfs(0, -1):
        return False

    # Check if all nodes were visited (i.e., the graph is connected)
    return len(visited) == n

# Time Complexity: O(n + e) - where n is the number of nodes and e is the number of edges
# Space Complexity: O(n + e) - for the graph and visited set

# Test the function with the example
print(valid_tree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]))  # Output: True
```

#### Alternative Approach:

- **Breadth-First Search (BFS)** can also be used to check for cycles and connectivity. Instead of using recursion, BFS uses a queue to iteratively explore the graph.

Here’s the BFS alternative approach:

```python
from collections import deque

def valid_tree_bfs(n, edges):
    if len(edges) != n - 1:
        return False  # A tree must have exactly n-1 edges

    # Build the adjacency list for the graph
    graph = {i: [] for i in range(n)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()
    queue = deque([0])
    visited.add(0)

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor in visited:
                continue  # Already visited, skip
            visited.add(neighbor)
            queue.append(neighbor)

    # Check if all nodes were visited
    return len(visited) == n

# Test the BFS function
print(valid_tree_bfs(5, [[0, 1], [0, 2], [0, 3], [1, 4]]))  # Output: True
```

---

### Problem 11: Number of Connected Components in an Undirected Graph

#### Problem Understanding:

- **Problem Explanation**: You are given an integer `n` representing the number of nodes, and an array `edges` where `edges[i] = [ai, bi]` represents an edge between nodes `ai` and `bi` in an undirected graph. Return the number of connected components in the graph.

**Example**:
Input:

```
n = 5
edges = [[0, 1], [1, 2], [3, 4]]
```

Output: `2`

#### Coding Pattern:

- We can use **Depth-First Search (DFS)** or **Breadth-First Search (BFS)** to explore all connected components in the graph. We start from each unvisited node and explore all nodes in its connected component, counting how many connected components exist.

#### Solution (DFS):

```python
def count_components(n, edges):
    # Build the adjacency list for the graph
    graph = {i: [] for i in range(n)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()
    component_count = 0

    # Helper function to perform DFS
    def dfs(node):
        visited.add(node)
        # Explore all the neighbors of the current node
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    # Perform DFS from every unvisited node
    for node in range(n):
        if node not in visited:
            dfs(node)
            component_count += 1  # Increment the count of connected components

    return component_count

# Time Complexity: O(n + e) - where n is the number of nodes and e is the number of edges
# Space Complexity: O(n + e) - for the graph and visited set

# Test the function with the example
print(count_components(5, [[0, 1], [1, 2], [3, 4]]))  # Output: 2
```

#### Alternative Approach:

- **Breadth-First Search (BFS)** can also be used to explore connected components. Here’s the BFS alternative approach:

```python
from collections import deque

def count_components_bfs(n, edges):
    # Build the adjacency list for the graph
    graph = {i: [] for i in range(n)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()
    component_count = 0

    # Perform BFS from every unvisited node
    def bfs(start):
        queue = deque([start])
        visited.add(start)
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

    for node in range(n):
        if node not in visited:
            bfs(node)
            component_count += 1  # Increment the count of connected components

    return component_count

# Test the BFS function
print(count_components_bfs(5, [[0, 1], [1, 2], [3, 4]]))  # Output: 2
```

---

### Problem 12: Redundant Connection

#### Problem Understanding:

- **Problem Explanation**: In this problem, a tree is a connected graph without cycles. You are given a graph that started as a tree with `n` nodes labeled from `1` to `n`, with one additional edge added. The task is to find the edge that can be removed so that the resulting graph remains a tree (no cycles).

**Example**:
Input:

```
edges = [[1, 2], [1, 3], [2, 3]]
```

Output: `[2, 3]`

#### Coding Pattern:

- This problem can be solved using **Union-Find (Disjoint Set)** to detect cycles. If adding an edge connects two nodes that are already connected (i.e., belong to the same set), then that edge creates a cycle and can be removed.

#### Solution:

```python
class UnionFind:
    def __init__(self, n):
        # Initialize each node to be its own parent (disjoint set)
        self.parent = list(range(n))
        self.rank = [1] * n  # Used for union by rank
  
    def find(self, node):
        # Find the root of the set containing the node (with path compression)
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
  
    def union(self, node1, node2):
        # Union by rank to merge two sets
        root1 = self.find(node1)
        root2 = self.find(node2)
        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1
        else:
            return False  # Cycle detected (nodes are already connected)
        return True

def find_redundant_connection(edges):
    uf = UnionFind(len(edges) + 1)  # Initialize union-find for n nodes (1-indexed)

    for u, v in edges:
        if not uf.union(u - 1, v - 1):  # Adjust for 0-based index
            return [u, v]  # Return the edge that forms a cycle

# Time Complexity: O(n) - where n is the number of edges
# Space Complexity: O(n) - for the Union-F

ind data structure

# Test the function with the example
print(find_redundant_connection([[1, 2], [1, 3], [2, 3]]))  # Output: [2, 3]
```

#### Alternative Approach:

- **No alternative approach**. The **Union-Find** (Disjoint Set) data structure is the most efficient solution for this problem as it efficiently detects cycles in an undirected graph.

---

### Problem 13: Word Ladder

#### Problem Understanding:

- **Problem Explanation**: Given two words, `beginWord` and `endWord`, and a dictionary's word list, return the length of the shortest transformation sequence from `beginWord` to `endWord`, such that:
  1. Only one letter can be changed at a time.
  2. Each transformed word must exist in the word list.

If there is no such transformation sequence, return `0`.

**Example**:
Input:

```
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
```

Output: `5`

#### Coding Pattern:

- This problem can be solved using **Breadth-First Search (BFS)**. Each word is treated as a node, and there is an edge between two nodes if they differ by exactly one letter. BFS ensures we find the shortest transformation path.

#### Solution:

```python
from collections import deque

def word_ladder(beginWord, endWord, wordList):
    wordSet = set(wordList)  # Convert the word list to a set for fast lookup
    if endWord not in wordSet:
        return 0  # If endWord is not in the list, there's no valid transformation

    # Initialize the BFS queue with the beginWord and transformation length 1
    queue = deque([(beginWord, 1)])

    while queue:
        current_word, steps = queue.popleft()

        # If the current word is the end word, return the number of steps
        if current_word == endWord:
            return steps

        # Try changing each letter of the current word
        for i in range(len(current_word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = current_word[:i] + c + current_word[i + 1:]
                if next_word in wordSet:
                    queue.append((next_word, steps + 1))  # Add the next word to the queue
                    wordSet.remove(next_word)  # Remove the word from the set to avoid revisiting

    return 0  # If no transformation is found, return 0

# Time Complexity: O(m * n) - where m is the length of the words and n is the number of words in the word list
# Space Complexity: O(m * n) - for the queue and word set

# Test the function with the example
print(word_ladder("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))  # Output: 5
```

#### Alternative Approach:

- **No alternative approach**. BFS is the best way to find the shortest path in this type of transformation problem where each node represents a word, and edges exist between words that differ by only one letter.

---

## Advanced Graphs

#### 1. **Reconstruct Itinerary** (Hard)

##### Problem Understanding:

You are given a list of airline tickets where `tickets[i] = [from_i, to_i]` represents a flight from `from_i` to `to_i`. Reconstruct the itinerary starting from "JFK". The output itinerary must follow the lexical order when multiple valid itineraries are possible.

##### Problem Explanation:

Given a list of tickets, each ticket represents a one-way flight between two cities. You must use all the tickets to form an itinerary, and the itinerary should start from "JFK". If there are multiple possible itineraries, return the one that is lexically smallest.

Example:

```
Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
```

##### Coding Pattern:

The problem can be solved using the **Hierholzer's Algorithm** (for Eulerian path/circuit in a graph). This is because every ticket must be used exactly once, and you are constructing a path.

##### Solution:

```python
from collections import defaultdict

def findItinerary(tickets):
    # Step 1: Build the graph to represent the flight routes
    graph = defaultdict(list)  # A dictionary where each key points to a list of destinations.
  
    # Step 2: Sort tickets by lexical order (reverse=True ensures that we can pop destinations in correct order)
    for origin, destination in sorted(tickets, reverse=True):
        graph[origin].append(destination)  # Append the destination to the list of possible flights from origin.
  
    result = []  # This will hold our final itinerary in reverse order.

    def visit(airport):
        # While there are destinations we can fly to from this airport
        while graph[airport]:
            next_dest = graph[airport].pop()  # Take the lexically smallest destination (since we sorted in reverse)
            visit(next_dest)  # Recursively visit the next airport
        result.append(airport)  # Once we can no longer fly anywhere from this airport, add it to the itinerary
  
    # Start DFS from 'JFK'
    visit('JFK')

    # Since the itinerary is built in reverse order, we reverse it at the end to get the correct order
    return result[::-1]

# Example test case
tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
print(findItinerary(tickets))  # Output: ['JFK', 'MUC', 'LHR', 'SFO', 'SJC']

```

##### Time Complexity:

- **Time**: `O(E log E)` where `E` is the number of edges (flights). Sorting all the destinations takes `E log E` time, and the DFS runs in linear time `O(E)`.
- **Space**: `O(V + E)` for storing the graph, where `V` is the number of vertices (airports) and `E` is the number of edges.

##### Alternative Approach:

There isn't a fundamentally different approach for this problem, as it specifically relies on traversing all tickets exactly once, but there could be optimizations or slight variations in the DFS.

---

#### 2. **Min Cost to Connect All Points** (Medium)

##### Problem Understanding:

You are given `n` points on a 2D plane. The task is to connect all the points such that the total cost is minimized. The cost of connecting two points `(x1, y1)` and `(x2, y2)` is the Manhattan distance `|x1 - x2| + |y1 - y2|`.

##### Problem Explanation:

We need to form a Minimum Spanning Tree (MST) to connect all points with minimum cost. The Manhattan distance between two points is the cost of the edge connecting those points.

Example:

```
Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
```

##### Coding Pattern:

This problem can be solved using **Kruskal’s Algorithm** or **Prim’s Algorithm**, which are both algorithms for finding the MST in a graph. We’ll use Prim’s Algorithm here.

##### Solution:

```python
import heapq  # To use a priority queue (min heap)

def minCostConnectPoints(points):
    n = len(points)  # Number of points
  
    # Helper function to calculate the Manhattan distance between two points
    def manhattan_dist(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
  
    # Step 1: Priority queue to hold the next point to be added to the MST (cost, point_index)
    pq = [(0, 0)]  # Start with the first point with a cost of 0
    in_mst = [False] * n  # Track which points are already included in the MST
    total_cost = 0  # Total cost to connect all points
    edges_used = 0  # Number of edges used to connect points
  
    # Step 2: Continue until we have added all points (n points means we need n-1 edges)
    while edges_used < n:
        cost, u = heapq.heappop(pq)  # Get the point with the smallest cost
      
        # Step 3: If this point is already in the MST, skip it
        if in_mst[u]:
            continue
      
        # Step 4: Otherwise, add this point to the MST
        in_mst[u] = True  # Mark the point as part of the MST
        total_cost += cost  # Add the cost of connecting this point
        edges_used += 1  # Increment the number of edges used
      
        # Step 5: Check all other points and calculate their distance from this point
        for v in range(n):
            if not in_mst[v]:  # If point v is not already in the MST
                dist = manhattan_dist(points[u], points[v])  # Calculate the Manhattan distance
                heapq.heappush(pq, (dist, v))  # Push this point and distance into the priority queue
  
    return total_cost  # Return the total cost to connect all points

# Example test case
points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
print(minCostConnectPoints(points))  # Output: 20

```

##### Time Complexity:

- **Time**: `O(n^2 log n)` where `n` is the number of points. We calculate the distance for each pair of points (n^2), and the priority queue operations take `log n` time.
- **Space**: `O(n^2)` for storing the distances between every pair of points.

##### Alternative Approach:

An alternative approach is to use **Kruskal’s Algorithm**, which sorts all edges and then connects the smallest available edge that doesn’t form a cycle. The time complexity is the same, but Prim’s is generally more efficient for dense graphs.

---

### 3. **Network Delay Time** (Medium)

#### Problem Explanation:

You are given a network with `n` nodes, labeled from `1` to `n`. Each directed edge `(u, v, w)` represents a signal taking `w` units of time to travel from node `u` to node `v`. Starting from node `k`, the goal is to find the minimum time it takes for the signal to reach all nodes. If it's impossible to reach all nodes, return `-1`.

#### Numeric Example:

```
Input: times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]], n = 4, k = 2
Output: 2

Explanation:
From node 2, the signal reaches:
- Node 1 in 1 unit of time.
- Node 3 in 1 unit of time.
- Node 4 in 2 units of time (travel through node 3).
Thus, the time for the signal to reach the farthest node (node 4) is 2 units.
```

#### Coding Pattern:

The problem can be solved using **Dijkstra's Algorithm**, which is a shortest-path algorithm. It is well-suited for this problem since we are looking for the minimum travel time from the starting node `k` to all other nodes in a weighted, directed graph.

#### Solution:

```python
import heapq  # To use a priority queue (min heap)

def networkDelayTime(times, n, k):
    # Step 1: Build the graph as an adjacency list
    graph = {i: [] for i in range(1, n+1)}  # Nodes are labeled from 1 to n
    for u, v, w in times:
        graph[u].append((v, w))  # Add an edge from u to v with weight w (time w)
  
    # Step 2: Priority queue to store (time, node), starting from the source node k
    pq = [(0, k)]  # (time to reach node, node) starting with 0 time from node k
    dist = {}  # Dictionary to track the shortest time to reach each node
  
    # Step 3: Use Dijkstra's algorithm to find the shortest path
    while pq:
        time, node = heapq.heappop(pq)  # Get the node with the smallest travel time
      
        # Skip if this node has already been processed
        if node in dist:
            continue
      
        # Record the time it takes to reach this node
        dist[node] = time
      
        # Step 4: Visit all neighbors of the current node
        for neighbor, weight in graph[node]:
            if neighbor not in dist:  # Only consider neighbors we haven't visited yet
                heapq.heappush(pq, (time + weight, neighbor))  # Push neighbor with updated time
  
    # Step 5: If all nodes are reachable, return the maximum time, otherwise return -1
    if len(dist) == n:
        return max(dist.values())  # Return the maximum time to reach any node
    else:
        return -1  # Not all nodes were reachable

# Example test case
times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
n = 4
k = 2
print(networkDelayTime(times, n, k))  # Output: 2
```

#### Time and Space Complexity:

```python
# Time Complexity: O(E log V), where E is the number of edges and V is the number of vertices (nodes).
# Each edge is processed once, and each time we process a node, we perform a heap operation that takes log V time.

# Space Complexity: O(V + E) for storing the graph (V nodes, E edges) and the distance dictionary.
```

#### Alternative Approach:

There is no significantly better alternative approach for this problem than **Dijkstra’s Algorithm**, as it is optimized for finding the shortest path in weighted graphs.

---

### 4. **Swim in Rising Water** (Hard)

#### Problem Explanation:

You are given an `n x n` grid, where each cell contains an integer representing the elevation at that point. The water in the grid rises, and at time `t`, the water has reached a level of `t`. You need to find the minimum time `t` required to swim from the top-left corner `(0, 0)` to the bottom-right corner `(n-1, n-1)`.

#### Numeric Example:

```
Input: grid = [[0, 2, 1], [1, 3, 2], [3, 4, 2]]
Output: 3

Explanation:
You can swim from (0, 0) to (2, 2) at time 3 by following the path:
(0, 0) -> (1, 0) -> (1, 1) -> (2, 1) -> (2, 2)
The maximum elevation encountered along the path is 3, which is the minimum time you can swim across.
```

#### Coding Pattern:

This problem can be solved using **Dijkstra’s Algorithm** or a **Priority Queue**-based **BFS** (Best First Search). The idea is to always explore the path that allows you to reach the next cell with the lowest possible maximum elevation encountered so far.

#### Solution:

```python
import heapq

def swimInWater(grid):
    n = len(grid)  # The size of the grid (n x n grid)
  
    # Step 1: Priority queue to store (time, row, col), starting from (0, 0)
    pq = [(grid[0][0], 0, 0)]  # (max elevation on the path so far, row, col)
    visited = set()  # To track visited cells
    visited.add((0, 0))  # Mark the starting cell as visited
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Possible movement directions: right, down, left, up
  
    # Step 2: Continue processing the priority queue
    while pq:
        elevation, r, c = heapq.heappop(pq)  # Get the cell with the smallest max elevation on the path
      
        # Step 3: If we've reached the bottom-right corner, return the time (elevation)
        if r == n-1 and c == n-1:
            return elevation
      
        # Step 4: Explore all 4 directions (right, down, left, up)
        for dr, dc in directions:
            nr, nc = r + dr, c + dc  # Calculate the new row and column
          
            # If the new cell is within bounds and hasn't been visited
            if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                visited.add((nr, nc))  # Mark the new cell as visited
                # Push the new cell into the queue with the max elevation seen so far
                heapq.heappush(pq, (max(elevation, grid[nr][nc]), nr, nc))

# Example test case
grid = [
    [0, 2, 1],
    [1, 3, 2],
    [3, 4, 2]
]
print(swimInWater(grid))  # Output: 3
```

#### Time and Space Complexity:

```python
# Time Complexity: O(n^2 log n), where n is the size of the grid. 
# There are n^2 cells, and each cell is processed with a heap operation that takes log n time.

# Space Complexity: O(n^2) for the priority queue and visited set.
```

#### Alternative Approach:

There are no significantly different alternative approaches for this problem. The priority queue-based approach is optimal for exploring paths with the smallest maximum elevation in such scenarios.

---

### 5. **Alien Dictionary** (Hard)

#### Problem Explanation:

You are given a list of words sorted in lexicographical order by an alien language. The goal is to derive the order of characters in this alien language. If no valid order exists, return an empty string.

#### Numeric Example:

```
Input: words = ["wrt", "wrf", "er", "ett", "rftt"]
Output: "wertf"

Explanation:
The order of characters is:
- 'w' comes before 'e'
- 'e' comes before 'r'
- 'r' comes before 't'
- 't' comes before 'f'
```

#### Coding Pattern:

This is a classic **Topological Sorting** problem, where you need to derive the order of elements based on pairwise dependencies. We can use **Kahn's Algorithm** (BFS) or **DFS** to solve the topological sort problem for directed acyclic graphs (DAGs).

#### Solution:

```python
from collections import defaultdict, deque

def alienOrder(words):
    # Step 1: Build the graph and indegree map
    graph = defaultdict(set)  # Adjacency list to store the graph
    indegree = {char: 0 for word in words for char in word}  # Indegree of each node

    # Step 2: Establish relationships between characters by comparing adjacent words
    for i in range(len(words) - 1):
        word1, word2 = words[i], words[i + 1]
        min_len = min(len(word1), len(word2))
      
        # Check if word2 is a valid prefix of word1 (invalid lexicographical order)
        if len(word1) > len(word2) and word1[:min_len] == word2:
            return ""  # Invalid order, return empty string
      
        # Find the first difference between the two words and create the edge
        for j in range(min_len):
            if word1[j] != word2[j]:
                if word2[j] not in graph[word1[j]]:
                    graph[word1[j]].add(word2[j])  # Create a directed edge
                    indegree[word2[j]] += 1  # Increment indegree of word2[j]
                break

    # Step 3: Perform topological sort using BFS (Kahn's Algorithm)
    # Initialize queue with all nodes having 0 indegree
    queue = deque([char for char in indegree if indegree[char] == 0])
    order = []  # To store the result of the topological sort
  
    while queue:
        char = queue.popleft()
        order.append(char)  # Add current char to the sorted order
      
        # Decrease indegree of all neighbors and add to queue if indegree becomes 0
        for neighbor in graph[char]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
  
    # If the number of characters in the result matches the number of unique characters, return the result
    if len(order) == len(indegree):
        return "".join(order)
    else:
        return ""  # Cycle detected, return empty string

# Example test case
words = ["wrt", "wrf", "er", "ett", "rftt"]
print(alienOrder(words))  # Output: "wertf"
```

#### Time and Space Complexity:

```python
# Time Complexity: O(C), where C is the total number of characters in all the words combined.
# We build the graph in O(C) time and perform topological sorting in O(C) time.

# Space Complexity: O(1) if we consider only the alphabet of 26 characters.
# Otherwise, it's O(C) for storing the graph and indegree information.
```

#### Alternative Approach:

We could also use **DFS** to implement the topological sort, but the overall complexity remains the same, and BFS (Kahn’s Algorithm) is generally more intuitive in this case.

---

### 6. **Cheapest Flights Within K Stops** (Medium)

#### Problem Explanation:

You are given a list of flights where `flights[i] = [from_i, to_i, price_i]` represents a flight from city `from_i` to city `to_i` with a price of `price_i`. You are also given the starting city `src`, the destination `dst`, and the number of stops `k`. The goal is to find the cheapest price to travel from `src` to `dst` with at most `k` stops. If no such route exists, return `-1`.

#### Numeric Example:

```
Input: n = 4, flights = [[0, 1, 100], [1, 2, 100], [2, 3, 100], [0, 2, 500]], src = 0, dst = 3, k = 1
Output: 300

Explanation:
The cheapest route is:
- Take flight 0 -> 1 (cost = 100), then flight 1 -> 2 (cost = 100), then flight 2 -> 3 (cost = 100)
Total cost = 300, with exactly 1 stop at city 2.
```

#### Coding Pattern:

This problem can be solved using **BFS** with a **Priority Queue** (similar to Dijkstra’s algorithm), but with an added constraint of `k` stops. Instead of finding the shortest path, we need to find the cheapest path under the given condition.

#### Solution:

```python
import heapq

def findCheapestPrice(n, flights, src, dst, k):
    # Step 1: Build the adjacency list for the graph
    graph = defaultdict(list)
    for u, v, price in flights:
        graph[u].append((v, price))
  
    # Step 2: Use a priority queue to perform BFS with the constraint of k stops
    pq = [(0, src, 0)]  # (current cost, current city, current number of stops)
    visited = {}  # Dictionary to track the minimum cost to reach a city with a certain number of stops
  
    while pq:
        cost, city, stops = heapq.heappop(pq)
      
        # If we reached the destination, return the cost
        if city == dst:
            return cost
      
        # If we have more stops available, continue exploring
        if stops <= k:
            for neighbor, price in graph[city]:
                new_cost = cost + price
                # Only add to the queue if it's the first visit or cheaper with fewer stops
                if (neighbor not in visited) or (visited[neighbor] > stops):
                    visited[neighbor] = stops
                    heapq.heappush(pq, (new_cost, neighbor, stops + 1))
  
    return -1  # If we cannot reach the destination within k stops

# Example test case
n = 4
flights = [[0, 1, 100], [1, 2, 100], [2, 3, 100], [0, 2, 500]]
src = 0
dst = 3
k = 1
print(findCheapestPrice(n, flights, src, dst, k))  # Output: 300
```

#### Time and Space Complexity:

```python
# Time Complexity: O(n^2 log n), where n is the number of cities.
# In the worst case, we explore all possible connections between cities.

# Space Complexity: O(n^2) for storing the graph and priority queue information.
```

#### Alternative Approach:

No other fundamentally different approach exists. The use of BFS with a priority queue is optimal for this type of problem, where we need to account for costs while restricting the number of steps.

---

## 1-D Dynamic Programming

### 7. **Climbing Stairs** (Easy)

#### Problem Explanation:

You are climbing a staircase with `n` steps. You can either take 1 step or 2 steps at a time. The task is to find the number of distinct ways you can reach the top.

#### Numeric Example:

```
Input: n = 3
Output: 3

Explanation:
- You can climb to the top in the following ways:
  1. (1 step) + (1 step) + (1 step)
  2. (1 step) + (2 steps)
  3. (2 steps) + (1 step)
So, there are 3 distinct ways to climb 3 steps.
```

#### Coding Pattern:

This problem can be solved using **Dynamic Programming**. It's similar to the Fibonacci sequence because, to reach step `n`, you can either come from step `n-1` (1 step) or step `n-2` (2 steps). Thus, the number of ways to reach step `n` is the sum of the ways to reach `n-1` and `n-2`.

#### Solution:

```python
def climbStairs(n):
    if n == 1:
        return 1  # Only 1 way to climb 1 step
  
    # Step 1: Initialize two base cases for dynamic programming
    prev1, prev2 = 2, 1  # prev1 is ways to reach step 2, prev2 is ways to reach step 1
  
    # Step 2: Use a bottom-up approach to calculate the number of ways to reach each step
    for i in range(3, n + 1):
        current = prev1 + prev2  # The number of ways to reach step i is the sum of the ways to reach i-1 and i-2
        prev2 = prev1  # Shift prev2 to prev1 for the next iteration
        prev1 = current  # Move current result to prev1 for the next iteration
  
    return prev1  # The answer for step n

# Example test case
n = 3
print(climbStairs(n))  # Output: 3
```

#### Time and Space Complexity:

```python
# Time Complexity: O(n), because we iterate through each step from 1 to n.

# Space Complexity: O(1), because we are using only two variables to store the intermediate results (constant space).
```

#### Alternative Approach:

No other fundamentally different approach exists, as **Dynamic Programming** is the optimal solution here. We could solve it using recursion with memoization, but the time and space complexity would remain the same.

---

### 8. **Min Cost Climbing Stairs** (Easy)

#### Problem Explanation:

You are given an array `cost` where `cost[i]` represents the cost of stepping on the `i`-th stair. Once you pay the cost, you can either move to the next stair or skip one stair. The task is to find the minimum cost required to reach the top of the staircase.

#### Numeric Example:

```
Input: cost = [10, 15, 20]
Output: 15

Explanation:
- Start on step 1 (cost = 15), then take a single step to the top (no cost).
- The total cost is 15.
```

#### Coding Pattern:

This problem can also be solved using **Dynamic Programming**. To find the minimum cost to reach the top from any step `i`, you need to consider the minimum cost from the previous two steps `i-1` and `i-2`, because you can either take 1 step or 2 steps.

#### Solution:

```python
def minCostClimbingStairs(cost):
    # Step 1: Initialize two base cases for dynamic programming
    prev1, prev2 = cost[1], cost[0]  # prev1 is cost to reach step 1, prev2 is cost to reach step 0
  
    # Step 2: Use a bottom-up approach to calculate the minimum cost for each step
    for i in range(2, len(cost)):
        current = min(prev1, prev2) + cost[i]  # Minimum cost to reach step i
        prev2 = prev1  # Shift prev2 to prev1 for the next iteration
        prev1 = current  # Move current result to prev1 for the next iteration
  
    # Step 3: Return the minimum cost of reaching the top from either the last step or the second last step
    return min(prev1, prev2)

# Example test case
cost = [10, 15, 20]
print(minCostClimbingStairs(cost))  # Output: 15
```

#### Time and Space Complexity:

```python
# Time Complexity: O(n), where n is the length of the cost array.

# Space Complexity: O(1), because we are using only two variables to store intermediate results.
```

#### Alternative Approach:

There’s no fundamentally different approach. A recursive solution with memoization can also be used, but the time and space complexity would remain the same.

---

### 9. **House Robber** (Medium)

#### Problem Explanation:

You are a robber planning to rob houses along a street. Each house has a certain amount of money, but adjacent houses have security systems connected. If you rob two adjacent houses, the alarm will be triggered. The task is to maximize the amount of money you can rob without triggering the alarm.

#### Numeric Example:

```
Input: nums = [2, 7, 9, 3, 1]
Output: 12

Explanation:
- Rob house 1 (money = 2), skip house 2, rob house 3 (money = 9), skip house 4, and rob house 5 (money = 1).
- The total amount robbed is 2 + 9 + 1 = 12.
```

#### Coding Pattern:

This problem is another example of **Dynamic Programming**. The key idea is that for each house `i`, you either rob that house and add its value to the total from `i-2` (since you cannot rob the adjacent house), or you skip it and take the maximum from `i-1`. Thus, the recurrence relation is: `dp[i] = max(dp[i-1], nums[i] + dp[i-2])`.

#### Solution:

```python
def rob(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
  
    # Step 1: Initialize two base cases
    prev1, prev2 = max(nums[0], nums[1]), nums[0]  # prev1 is max at step 1, prev2 is max at step 0
  
    # Step 2: Use a bottom-up approach to calculate the maximum amount of money that can be robbed
    for i in range(2, len(nums)):
        current = max(prev1, prev2 + nums[i])  # Max value at house i is either robbing it or skipping it
        prev2 = prev1  # Shift prev2 to prev1 for the next iteration
        prev1 = current  # Move current result to prev1 for the next iteration
  
    return prev1

# Example test case
nums = [2, 7, 9, 3, 1]
print(rob(nums))  # Output: 12
```

#### Time and Space Complexity:

```python
# Time Complexity: O(n), where n is the length of the nums array.

# Space Complexity: O(1), because we are using only two variables to store the intermediate results.
```

#### Alternative Approach:

A recursive solution with memoization can also be used to solve this problem, but it would have a similar time complexity of `O(n)` and a space complexity of `O(n)` due to the recursion stack.

---

Let's continue with the next set of problems.

---

### 10. **House Robber II** (Medium)

#### Problem Explanation:

This problem is a variation of the **House Robber** problem. Now, the houses are arranged in a circle, meaning the first and last houses are adjacent. The task is to maximize the amount of money you can rob without robbing two adjacent houses, taking the circular arrangement into account.

#### Numeric Example:

```
Input: nums = [2, 3, 2]
Output: 3

Explanation:
- You can either rob house 1 (money = 2) and house 3 (money = 2), or rob house 2 (money = 3). 
- The maximum money you can rob is 3.
```

#### Coding Pattern:

This problem can be solved using **Dynamic Programming** similar to **House Robber**. However, because the first and last houses are adjacent, we need to consider two scenarios:

1. Rob houses from the first house to the second last house.
2. Rob houses from the second house to the last house.
   The solution is the maximum result from these two scenarios.

#### Solution:

```python
def rob_helper(nums):
    # Helper function to perform the normal House Robber logic
    if len(nums) == 1:
        return nums[0]
  
    prev1, prev2 = max(nums[0], nums[1]), nums[0]
  
    for i in range(2, len(nums)):
        current = max(prev1, prev2 + nums[i])
        prev2 = prev1
        prev1 = current
  
    return prev1

def rob(nums):
    if len(nums) == 1:
        return nums[0]
  
    # Step 1: Consider robbing houses from the first house to the second last house
    case1 = rob_helper(nums[:-1])  # Exclude the last house
  
    # Step 2: Consider robbing houses from the second house to the last house
    case2 = rob_helper(nums[1:])  # Exclude the first house
  
    # Step 3: The maximum result is the answer
    return max(case1, case2)

# Example test case
nums = [2, 3, 2]
print(rob(nums))  # Output: 3
```

#### Time and Space Complexity:

```python
# Time Complexity: O(n), where n is the length of the nums array.
# We perform two runs of the House Robber algorithm (linear time).

# Space Complexity: O(1), because we are using only two variables to store intermediate results in the helper function.
```

#### Alternative Approach:

There is no significantly different alternative approach for this problem. We could solve this with recursion and memoization, but it would still be `O(n)` in time complexity and `O(n)` in space complexity due to the recursion stack.

---

### 11. **Longest Palindromic Substring** (Medium)

#### Problem Explanation:

Given a string `s`, find the longest palindromic substring in `s`.

#### Numeric Example:

```
Input: s = "babad"
Output: "bab"

Explanation:
- "bab" is a palindrome, and it is the longest palindromic substring in the input string.
- Note: "aba" is also a valid answer.
```

#### Coding Pattern:

This problem can be solved using the **Expand Around Center** approach. A palindrome mirrors around its center. To find all palindromes, we can expand around every possible center of the string (which can be between two characters or at a character itself).

#### Solution:

```python
def longestPalindrome(s):
    if len(s) == 0:
        return ""
  
    def expandAroundCenter(s, left, right):
        # Expand around the given center and return the longest palindrome
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]  # Return the valid palindrome
  
    longest = ""
  
    # Step 1: Consider each character and each pair of characters as a center and expand around it
    for i in range(len(s)):
        # Odd-length palindromes (centered at a single character)
        odd_palindrome = expandAroundCenter(s, i, i)
        if len(odd_palindrome) > len(longest):
            longest = odd_palindrome
      
        # Even-length palindromes (centered between two characters)
        even_palindrome = expandAroundCenter(s, i, i + 1)
        if len(even_palindrome) > len(longest):
            longest = even_palindrome
  
    return longest

# Example test case
s = "babad"
print(longestPalindrome(s))  # Output: "bab"
```

#### Time and Space Complexity:

```python
# Time Complexity: O(n^2), where n is the length of the string.
# We expand around each possible center, and each expansion can take O(n) time.

# Space Complexity: O(1), because we are only using a few extra variables (constant space).
```

#### Alternative Approach:

A **Dynamic Programming** approach can also be used to solve this problem by keeping track of whether a substring is a palindrome. However, the time complexity remains `O(n^2)` due to the nested loops, and the space complexity is `O(n^2)` due to the DP table. The **Expand Around Center** approach is generally preferred for its simplicity.

---

### 12. **Palindromic Substrings** (Medium)

#### Problem Explanation:

Given a string `s`, return the number of palindromic substrings in `s`.

#### Numeric Example:

```
Input: s = "aaa"
Output: 6

Explanation:
The palindromic substrings are "a", "a", "a", "aa", "aa", and "aaa".
```

#### Coding Pattern:

This problem can also be solved using the **Expand Around Center** approach. For each center in the string, we can expand outwards and count all valid palindromes.

#### Solution:

```python
def countSubstrings(s):
    def expandAroundCenter(s, left, right):
        count = 0
        # Expand around the given center and count palindromes
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        return count
  
    total_palindromes = 0
  
    # Step 1: Consider each character and each pair of characters as a center and expand around it
    for i in range(len(s)):
        total_palindromes += expandAroundCenter(s, i, i)  # Odd-length palindromes
        total_palindromes += expandAroundCenter(s, i, i + 1)  # Even-length palindromes
  
    return total_palindromes

# Example test case
s = "aaa"
print(countSubstrings(s))  # Output: 6
```

#### Time and Space Complexity:

```python
# Time Complexity: O(n^2), where n is the length of the string.
# We expand around each possible center, and each expansion can take O(n) time.

# Space Complexity: O(1), because we are only using a few extra variables (constant space).
```

#### Alternative Approach:

We can solve this problem using a **Dynamic Programming** approach, where we build a DP table that tracks whether a substring is a palindrome. This would also have `O(n^2)` time and space complexity, but the **Expand Around Center** approach is simpler.

---

Let's continue with the next set of problems following the same detailed format.

---

### 13. **Decode Ways** (Medium)

#### Problem Explanation:

A message containing letters from A-Z is encoded as follows:

- 'A' -> "1"
- 'B' -> "2"
- ...
- 'Z' -> "26"

You are given a string `s` representing the encoded message. The task is to determine the total number of ways to decode it.

#### Numeric Example:

```
Input: s = "226"
Output: 3

Explanation:
The string "226" can be decoded as:
- "B" -> "2" and "B" -> "2" and "F" -> "6" (i.e., "BBF")
- "B" -> "2" and "V" -> "26" (i.e., "BV")
- "Z" -> "22" and "6" -> "6" (i.e., "ZZ")
```

#### Coding Pattern:

This problem can be solved using **Dynamic Programming**. We keep track of the number of ways to decode the string up to each character. For each character, we check if it can be decoded as a single digit or a valid two-digit number.

#### Solution:

```python
def numDecodings(s):
    if not s or s[0] == '0':  # No valid decoding if the string starts with '0'
        return 0
  
    # Step 1: Initialize dp array to store the number of ways to decode up to each index
    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1  # Base case: an empty string has 1 way to be decoded
    dp[1] = 1 if s[0] != '0' else 0  # The first character must not be '0' for a valid decoding
  
    # Step 2: Fill the dp array using the recursive relation
    for i in range(2, n + 1):
        one_digit = int(s[i-1:i])  # Single digit number (last character)
        two_digits = int(s[i-2:i])  # Two digit number (last two characters)
      
        if 1 <= one_digit <= 9:  # If the single digit number is valid (1-9)
            dp[i] += dp[i-1]
      
        if 10 <= two_digits <= 26:  # If the two-digit number is valid (10-26)
            dp[i] += dp[i-2]
  
    return dp[n]

# Example test case
s = "226"
print(numDecodings(s))  # Output: 3
```

#### Time and Space Complexity:

```python
# Time Complexity: O(n), where n is the length of the input string.
# We process each character of the string exactly once.

# Space Complexity: O(n), because we use a dp array of size n + 1 to store the results.
```

#### Alternative Approach:

The space complexity can be reduced to `O(1)` by using two variables to store only the last two results instead of the entire dp array. Here's the space-optimized approach:

```python
def numDecodings(s):
    if not s or s[0] == '0':
        return 0
  
    n = len(s)
    prev2, prev1 = 1, 1  # Base cases for dp[-2] and dp[-1]
  
    for i in range(1, n):
        current = 0
        one_digit = int(s[i:i+1])
        two_digits = int(s[i-1:i+1])
      
        if 1 <= one_digit <= 9:
            current += prev1
      
        if 10 <= two_digits <= 26:
            current += prev2
      
        prev2, prev1 = prev1, current  # Move the previous values forward
  
    return prev1
```

---

### 14. **Coin Change** (Medium)

#### Problem Explanation:

You are given an integer array `coins` representing different denominations of coins and an integer `amount` representing a total amount of money. The task is to find the fewest number of coins needed to make up that amount. If it's not possible to make the amount, return `-1`.

#### Numeric Example:

```
Input: coins = [1, 2, 5], amount = 11
Output: 3

Explanation:
To make amount 11, we can use three coins: 5 + 5 + 1.
```

#### Coding Pattern:

This problem can be solved using **Dynamic Programming**. We need to find the minimum number of coins for every amount from `0` to `amount`. The recurrence relation is: `dp[i] = min(dp[i], dp[i - coin] + 1)` for every coin.

#### Solution:

```python
def coinChange(coins, amount):
    # Step 1: Initialize dp array with an initial value higher than any possible number of coins
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # Base case: it takes 0 coins to make amount 0
  
    # Step 2: Fill the dp array using the recursive relation
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)  # Take the minimum number of coins for amount i
  
    # Step 3: Return the result, if dp[amount] is still infinity, it means it's not possible to make the amount
    return dp[amount] if dp[amount] != float('inf') else -1

# Example test case
coins = [1, 2, 5]
amount = 11
print(coinChange(coins, amount))  # Output: 3
```

#### Time and Space Complexity:

```python
# Time Complexity: O(n * m), where n is the amount and m is the number of coins.
# We fill the dp array of size n for each coin.

# Space Complexity: O(n), because we use a dp array of size amount + 1.
```

#### Alternative Approach:

There is no fundamentally different alternative approach for this problem that improves upon **Dynamic Programming**. We could use BFS to explore all possible combinations of coins, but it would have similar time complexity.

---

### 15. **Maximum Product Subarray** (Medium)

#### Problem Explanation:

Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest product.

#### Numeric Example:

```
Input: nums = [2, 3, -2, 4]
Output: 6

Explanation:
The subarray [2, 3] has the largest product 6.
```

#### Coding Pattern:

This problem can be solved using **Dynamic Programming** with a twist. We need to keep track of both the maximum and minimum product at each position because multiplying a negative number by the minimum product can result in the maximum product.

#### Solution:

```python
def maxProduct(nums):
    if not nums:
        return 0
  
    # Step 1: Initialize the maximum and minimum products at the first position
    max_prod = min_prod = result = nums[0]
  
    # Step 2: Traverse the array and update the maximum and minimum products at each step
    for i in range(1, len(nums)):
        if nums[i] < 0:  # If the current number is negative, swap the max and min
            max_prod, min_prod = min_prod, max_prod
      
        max_prod = max(nums[i], max_prod * nums[i])
        min_prod = min(nums[i], min_prod * nums[i])
      
        result = max(result, max_prod)
  
    return result

# Example test case
nums = [2, 3, -2, 4]
print(maxProduct(nums))  # Output: 6
```

#### Time and Space Complexity:

```python
# Time Complexity: O(n), where n is the length of the input array.
# We iterate through the array once to calculate the maximum product.

# Space Complexity: O(1), because we are using only a few variables to store the results.
```

#### Alternative Approach:

There is no significantly different approach that improves upon this **Dynamic Programming** solution. The space complexity is already optimized to `O(1)`.

---

Let's continue with the next set of problems in the same detailed format.

---

### 16. **Word Break** (Medium)

#### Problem Explanation:

You are given a string `s` and a dictionary of words `wordDict`. Determine if `s` can be segmented into a space-separated sequence of one or more dictionary words. The same word in the dictionary may be reused multiple times in the segmentation.

#### Numeric Example:

```
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true

Explanation:
The string "leetcode" can be segmented as "leet code".
```

#### Coding Pattern:

This is a classic **Dynamic Programming** problem. We use a `dp` array where `dp[i]` indicates whether the substring `s[0:i]` can be segmented using the dictionary. For each position `i`, we check all possible words in the dictionary and see if `dp[j]` is `True` for any valid prefix `s[0:j]`.

#### Solution:

```python
def wordBreak(s, wordDict):
    # Step 1: Convert the wordDict to a set for faster lookup
    word_set = set(wordDict)
  
    # Step 2: Initialize a dp array where dp[i] indicates whether s[0:i] can be segmented
    dp = [False] * (len(s) + 1)
    dp[0] = True  # Base case: an empty string can always be segmented
  
    # Step 3: Fill the dp array by checking each substring s[j:i]
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
  
    return dp[len(s)]  # The result is whether the entire string can be segmented

# Example test case
s = "leetcode"
wordDict = ["leet", "code"]
print(wordBreak(s, wordDict))  # Output: True
```

#### Time and Space Complexity:

```python
# Time Complexity: O(n^2), where n is the length of the input string.
# We check every substring s[j:i] for each index i, and checking whether a word exists in the dictionary takes O(1) with a set.

# Space Complexity: O(n), where n is the length of the input string.
# We use a dp array of size n+1.
```

#### Alternative Approach:

There is no significantly different alternative approach for this problem that improves upon **Dynamic Programming**. We could use recursion with memoization to achieve the same result.

---

### 17. **Longest Increasing Subsequence** (Medium)

#### Problem Explanation:

Given an integer array `nums`, return the length of the longest strictly increasing subsequence.

#### Numeric Example:

```
Input: nums = [10, 9, 2, 5, 3, 7, 101, 18]
Output: 4

Explanation:
The longest increasing subsequence is [2, 3, 7, 101], so the length is 4.
```

#### Coding Pattern:

This problem can be solved using **Dynamic Programming**. We maintain a `dp` array where `dp[i]` represents the length of the longest increasing subsequence ending at index `i`. For each index `i`, we check all previous indices `j < i` and update `dp[i]` based on whether `nums[i] > nums[j]`.

#### Solution:

```python
def lengthOfLIS(nums):
    if not nums:
        return 0
  
    # Step 1: Initialize dp array where dp[i] represents the LIS ending at index i
    dp = [1] * len(nums)  # Every element is its own subsequence of length 1
  
    # Step 2: Fill the dp array by checking previous elements for each i
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
  
    return max(dp)  # The answer is the maximum value in dp

# Example test case
nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(lengthOfLIS(nums))  # Output: 4
```

#### Time and Space Complexity:

```python
# Time Complexity: O(n^2), where n is the length of the input array.
# We compare every pair of indices i and j.

# Space Complexity: O(n), because we use a dp array of size n to store the results.
```

#### Alternative Approach:

A more optimized approach involves using **Binary Search** and a greedy algorithm. Instead of maintaining a `dp` array, we use a list to keep track of the smallest possible ending values of increasing subsequences of various lengths. The time complexity for this approach is `O(n log n)`.

Here’s the optimized solution:

```python
import bisect

def lengthOfLIS(nums):
    if not nums:
        return 0
  
    # Step 1: Use a list to keep track of the smallest possible ending values
    lis = []
  
    # Step 2: Traverse the array and maintain the lis using binary search
    for num in nums:
        pos = bisect.bisect_left(lis, num)
        if pos < len(lis):
            lis[pos] = num  # Replace the current value with the new one
        else:
            lis.append(num)  # Extend the lis with the new number
  
    return len(lis)

# Example test case
nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(lengthOfLIS(nums))  # Output: 4
```

---

### 18. **Partition Equal Subset Sum** (Medium)

#### Problem Explanation:

Given a non-empty array `nums` containing positive integers, determine if you can partition the array into two subsets such that the sum of elements in both subsets is equal.

#### Numeric Example:

```
Input: nums = [1, 5, 11, 5]
Output: true

Explanation:
The array can be partitioned as [1, 5, 5] and [11].
```

#### Coding Pattern:

This is another classic **Dynamic Programming** problem. It’s equivalent to the subset sum problem. We want to find if there exists a subset whose sum equals `total_sum / 2`, where `total_sum` is the sum of all elements in the array. If `total_sum` is odd, it's impossible to partition the array, so we return `False`.

#### Solution:

```python
def canPartition(nums):
    total_sum = sum(nums)
  
    # Step 1: If the total sum is odd, it's impossible to partition it into two equal subsets
    if total_sum % 2 != 0:
        return False
  
    target = total_sum // 2
  
    # Step 2: Initialize a dp array where dp[i] indicates whether we can achieve sum i
    dp = [False] * (target + 1)
    dp[0] = True  # Base case: we can always form the sum 0 by choosing no elements
  
    # Step 3: For each number in nums, update the dp array
    for num in nums:
        # Traverse the dp array backwards to avoid overwriting results for the current iteration
        for i in range(target, num - 1, -1):
            dp[i] = dp[i] or dp[i - num]
  
    return dp[target]

# Example test case
nums = [1, 5, 11, 5]
print(canPartition(nums))  # Output: True
```

#### Time and Space Complexity:

```python
# Time Complexity: O(n * target), where n is the number of elements and target is the sum of half the total array.

# Space Complexity: O(target), because we use a dp array of size target + 1.
```

#### Alternative Approach:

There is no fundamentally different approach, but you could use recursion with memoization to solve this problem. However, it would have a similar time complexity of `O(n * target)`.

---

## 2-D Dynamic Programming

### 1. **Unique Paths** (Medium)

#### Problem Explanation:

You are given an `m x n` grid, and you are a robot located at the top-left corner. Your goal is to reach the bottom-right corner. You can only move either down or right. The task is to find how many unique paths there are from the top-left corner to the bottom-right corner.

#### Numeric Example:

```
Input: m = 3, n = 7
Output: 28

Explanation:
There are 28 unique paths from the top-left to the bottom-right in a 3x7 grid.
```

#### Coding Pattern:

This problem can be solved using **Dynamic Programming**. We maintain a 2D `dp` array where `dp[i][j]` represents the number of unique paths to reach the cell `(i, j)` from the top-left corner. The recurrence relation is:

```
dp[i][j] = dp[i-1][j] + dp[i][j-1]
```

since you can either come from the top or from the left.

#### Solution:

```python
def uniquePaths(m, n):
    # Step 1: Initialize a 2D dp array with all elements set to 1
    dp = [[1] * n for _ in range(m)]
  
    # Step 2: Fill the dp array using the recurrence relation
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
  
    # Step 3: The bottom-right corner contains the total number of unique paths
    return dp[m-1][n-1]

# Example test case
m = 3
n = 7
print(uniquePaths(m, n))  # Output: 28
```

#### Time and Space Complexity:

```python
# Time Complexity: O(m * n), because we fill a 2D array of size m * n.

# Space Complexity: O(m * n), because we use a 2D array to store the number of unique paths for each cell.
```

#### Alternative Approach:

A more optimized solution involves reducing the space complexity to `O(n)` by only maintaining the current and previous row in a 1D array, as we only need the previous row to compute the current one.

Here’s the space-optimized approach:

```python
def uniquePaths(m, n):
    # Step 1: Initialize a 1D dp array with all elements set to 1
    dp = [1] * n
  
    # Step 2: Update the dp array for each row
    for i in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j-1]  # Add the value from the left to the current cell
  
    # Step 3: The last element contains the total number of unique paths
    return dp[n-1]

# Example test case
m = 3
n = 7
print(uniquePaths(m, n))  # Output: 28
```

---

### 2. **Longest Common Subsequence** (Medium)

#### Problem Explanation:

Given two strings `text1` and `text2`, return the length of their longest common subsequence. A subsequence is a sequence that appears in the same relative order but not necessarily contiguously.

#### Numeric Example:

```
Input: text1 = "abcde", text2 = "ace"
Output: 3

Explanation:
The longest common subsequence is "ace" with length 3.
```

#### Coding Pattern:

This problem can be solved using **Dynamic Programming**. We maintain a 2D `dp` array where `dp[i][j]` represents the length of the longest common subsequence of `text1[0:i]` and `text2[0:j]`. The recurrence relation is:

```
if text1[i-1] == text2[j-1]:
    dp[i][j] = dp[i-1][j-1] + 1
else:
    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
```

#### Solution:

```python
def longestCommonSubsequence(text1, text2):
    m, n = len(text1), len(text2)
  
    # Step 1: Initialize a 2D dp array with dimensions (m+1) x (n+1)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
  
    # Step 2: Fill the dp array using the recurrence relation
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
  
    # Step 3: The bottom-right corner contains the length of the LCS
    return dp[m][n]

# Example test case
text1 = "abcde"
text2 = "ace"
print(longestCommonSubsequence(text1, text2))  # Output: 3
```

#### Time and Space Complexity:

```python
# Time Complexity: O(m * n), where m is the length of text1 and n is the length of text2.

# Space Complexity: O(m * n), because we use a 2D array to store the LCS for each substring.
```

#### Alternative Approach:

The space complexity can be reduced to `O(min(m, n))` by only maintaining the current and previous row in a 1D array, as we only need the values from the previous row to compute the current row.

Here’s the space-optimized approach:

```python
def longestCommonSubsequence(text1, text2):
    if len(text1) < len(text2):
        text1, text2 = text2, text1  # Ensure text1 is the longer string
  
    previous = [0] * (len(text2) + 1)
  
    # Step 1: Update the dp array row by row
    for i in range(1, len(text1) + 1):
        current = [0] * (len(text2) + 1)
        for j in range(1, len(text2) + 1):
            if text1[i - 1] == text2[j - 1]:
                current[j] = previous[j - 1] + 1
            else:
                current[j] = max(previous[j], current[j - 1])
        previous = current
  
    return previous[len(text2)]

# Example test case
text1 = "abcde"
text2 = "ace"
print(longestCommonSubsequence(text1, text2))  # Output: 3
```

---

Let's continue with the next set of problems from the **2-D Dynamic Programming** section.

---

### 3. **Best Time to Buy and Sell Stock with Cooldown** (Medium)

#### Problem Explanation:

You are given an array where each element represents the price of a stock on a given day. You can buy and sell the stock multiple times, but after you sell the stock, you cannot buy again for one day (cooldown). The task is to maximize your profit.

#### Numeric Example:

```
Input: prices = [1, 2, 3, 0, 2]
Output: 3

Explanation:
- Buy on day 0 (price = 1), sell on day 2 (price = 3), cooldown on day 3, and buy on day 4, then sell on day 4 (price = 2).
- Total profit = (3 - 1) + (2 - 0) = 3.
```

#### Coding Pattern:

This problem can be solved using **Dynamic Programming**. We define three states:

1. `hold[i]`: the maximum profit on day `i` if we hold a stock.
2. `sold[i]`: the maximum profit on day `i` if we just sold a stock.
3. `rest[i]`: the maximum profit on day `i` if we are in cooldown.

The recurrence relations are:

```
hold[i] = max(hold[i-1], rest[i-1] - prices[i])  # Either keep holding or buy a new stock
sold[i] = hold[i-1] + prices[i]  # Sell the stock we were holding
rest[i] = max(rest[i-1], sold[i-1])  # Either stay in cooldown or just sold the previous day
```

#### Solution:

```python
def maxProfit(prices):
    if not prices:
        return 0
  
    n = len(prices)
  
    # Step 1: Initialize the states
    hold = [0] * n
    sold = [0] * n
    rest = [0] * n
  
    hold[0] = -prices[0]  # On day 0, the only option is to buy the stock
  
    # Step 2: Fill the dp arrays using the recurrence relations
    for i in range(1, n):
        hold[i] = max(hold[i-1], rest[i-1] - prices[i])
        sold[i] = hold[i-1] + prices[i]
        rest[i] = max(rest[i-1], sold[i-1])
  
    # Step 3: The maximum profit will be the maximum of either selling or resting on the last day
    return max(sold[-1], rest[-1])

# Example test case
prices = [1, 2, 3, 0, 2]
print(maxProfit(prices))  # Output: 3
```

#### Time and Space Complexity:

```python
# Time Complexity: O(n), where n is the number of days (length of prices).
# We iterate through the prices array once.

# Space Complexity: O(n), because we use three arrays of size n to store the states.
```

#### Alternative Approach:

The space complexity can be reduced to `O(1)` by using only variables to store the current and previous states instead of entire arrays.

Here’s the space-optimized approach:

```python
def maxProfit(prices):
    if not prices:
        return 0
  
    hold = -prices[0]
    sold = 0
    rest = 0
  
    # Step 1: Iterate over the prices and update the states
    for i in range(1, len(prices)):
        prev_hold, prev_sold, prev_rest = hold, sold, rest
        hold = max(prev_hold, prev_rest - prices[i])
        sold = prev_hold + prices[i]
        rest = max(prev_rest, prev_sold)
  
    return max(sold, rest)

# Example test case
prices = [1, 2, 3, 0, 2]
print(maxProfit(prices))  # Output: 3
```

---

### 4. **Coin Change II** (Medium)

#### Problem Explanation:

You are given an integer array `coins` representing different denominations of coins and an integer `amount` representing a total amount of money. The task is to count the number of different ways to make up the amount using the available coins. The order of coins does not matter.

#### Numeric Example:

```
Input: amount = 5, coins = [1, 2, 5]
Output: 4

Explanation:
There are 4 ways to make the amount 5:
1. 5
2. 2 + 2 + 1
3. 2 + 1 + 1 + 1
4. 1 + 1 + 1 + 1 + 1
```

#### Coding Pattern:

This problem is solved using **Dynamic Programming** similar to the "Knapsack Problem". We use a `dp` array where `dp[i]` represents the number of ways to make the amount `i`. For each coin, we iterate through all possible amounts and update the number of ways to form the amount using that coin.

#### Solution:

```python
def change(amount, coins):
    # Step 1: Initialize a dp array of size amount+1 with dp[0] = 1
    dp = [0] * (amount + 1)
    dp[0] = 1  # There is one way to make amount 0, by using no coins
  
    # Step 2: Iterate over each coin and update the dp array
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]  # Update the number of ways to form amount i
  
    return dp[amount]

# Example test case
amount = 5
coins = [1, 2, 5]
print(change(amount, coins))  # Output: 4
```

#### Time and Space Complexity:

```python
# Time Complexity: O(n * m), where n is the amount and m is the number of coins.
# We iterate through the dp array for each coin.

# Space Complexity: O(n), because we use a dp array of size amount+1.
```

#### Alternative Approach:

There is no fundamentally different approach. This dynamic programming method efficiently solves the problem in linear space and time complexity.

---

### 5. **Target Sum** (Medium)

#### Problem Explanation:

You are given an integer array `nums` and an integer `S`. Each element in the array can either be assigned a positive or negative sign. The task is to find the number of ways to assign the signs such that the sum of the elements is equal to `S`.

#### Numeric Example:

```
Input: nums = [1, 1, 1, 1, 1], S = 3
Output: 5

Explanation:
There are 5 ways to assign signs to make the sum equal to 3:
1. +1 -1 +1 +1 +1
2. -1 +1 +1 +1 +1
3. +1 +1 -1 +1 +1
4. +1 +1 +1 -1 +1
5. +1 +1 +1 +1 -1
```

#### Coding Pattern:

This problem can be transformed into a **Subset Sum** problem. The key idea is to partition the array into two subsets where the difference between their sums equals `S`. We use **Dynamic Programming** to solve this.

The problem becomes finding subsets with sum `(sum(nums) + S) // 2`. If this value is not an integer or if `sum(nums) + S` is odd, there is no solution.

#### Solution:

```python
def findTargetSumWays(nums, S):
    total_sum = sum(nums)
  
    # Step 1: If the sum of nums + S is odd or if S > total_sum, return 0
    if total_sum < S or (total_sum + S) % 2 != 0:
        return 0
  
    target = (total_sum + S) // 2
  
    # Step 2: Initialize a dp array where dp[i] represents the number of ways to form sum i
    dp = [0] * (target + 1)
    dp[0] = 1  # There is one way to form sum 0, by using no elements
  
    # Step 3: Iterate over nums and update the dp array
    for num in nums:
        for i in range(target, num - 1, -1):
            dp[i] += dp[i - num]
  
    return dp[target]

# Example test case
nums = [1, 1, 1, 1, 1]
S = 3
print(findTargetSumWays(nums, S))  # Output: 5
```

#### Time and Space Complexity:

```python
# Time Complexity: O(n * target), where n is the number of elements and target is the new target sum.

# Space Complexity: O(target), because we use a dp array of size target+1.
```

#### Alternative Approach:

There is no fundamentally different approach, though recursion with memoization could be used. However, this dynamic programming approach is more efficient for this type of problem.

---

Let's continue with the next set of problems from the **2-D Dynamic Programming** section.

---

### 6. **Interleaving String** (Medium)

#### Problem Explanation:

Given three strings `s1`, `s2`, and `s3`, determine if `s3` is formed by an interleaving of `s1` and `s2`. An interleaving of two strings maintains the order of the characters from each string but mixes them together.

#### Numeric Example:

```
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true

Explanation:
"s3" can be formed by interleaving "aabcc" and "dbbca".
```

#### Coding Pattern:

This problem can be solved using **Dynamic Programming**. We define a 2D `dp` array where `dp[i][j]` indicates whether `s3[0:i+j]` can be formed by interleaving `s1[0:i]` and `s2[0:j]`. The recurrence relation is:

```
dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1])
```

#### Solution:

```python
def isInterleave(s1, s2, s3):
    if len(s1) + len(s2) != len(s3):
        return False
  
    # Step 1: Initialize a 2D dp array where dp[i][j] means s3[0:i+j] can be formed
    dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    dp[0][0] = True  # Base case: an empty s1 and s2 can form an empty s3
  
    # Step 2: Fill the dp array
    for i in range(len(s1) + 1):
        for j in range(len(s2) + 1):
            if i > 0:
                dp[i][j] = dp[i][j] or (dp[i-1][j] and s1[i-1] == s3[i+j-1])
            if j > 0:
                dp[i][j] = dp[i][j] or (dp[i][j-1] and s2[j-1] == s3[i+j-1])
  
    return dp[len(s1)][len(s2)]

# Example test case
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
print(isInterleave(s1, s2, s3))  # Output: True
```

#### Time and Space Complexity:

```python
# Time Complexity: O(m * n), where m is the length of s1 and n is the length of s2.
# We fill a 2D array of size (m+1) x (n+1).

# Space Complexity: O(m * n), because we use a 2D array to store the results for each substring combination.
```

#### Alternative Approach:

The space complexity can be optimized to `O(n)` by only maintaining the current and previous rows of the `dp` array, as we only need the previous row to compute the current one.

Here’s the space-optimized approach:

```python
def isInterleave(s1, s2, s3):
    if len(s1) + len(s2) != len(s3):
        return False
  
    dp = [False] * (len(s2) + 1)
    dp[0] = True
  
    for j in range(1, len(s2) + 1):
        dp[j] = dp[j-1] and s2[j-1] == s3[j-1]
  
    for i in range(1, len(s1) + 1):
        dp[0] = dp[0] and s1[i-1] == s3[i-1]
        for j in range(1, len(s2) + 1):
            dp[j] = (dp[j] and s1[i-1] == s3[i+j-1]) or (dp[j-1] and s2[j-1] == s3[i+j-1])
  
    return dp[len(s2)]

# Example test case
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
print(isInterleave(s1, s2, s3))  # Output: True
```

---

### 7. **Longest Increasing Path in a Matrix** (Hard)

#### Problem Explanation:

Given an `m x n` matrix of integers, return the length of the longest increasing path in the matrix. You can move in four directions: up, down, left, or right, and you may not move diagonally or outside the boundary of the matrix.

#### Numeric Example:

```
Input: matrix = [
  [9, 9, 4],
  [6, 6, 8],
  [2, 1, 1]
]
Output: 4

Explanation:
The longest increasing path is [1, 2, 6, 9].
```

#### Coding Pattern:

This problem can be solved using **Dynamic Programming** with **DFS** and memoization. For each cell, we explore all four possible directions and compute the longest increasing path starting from that cell. We use memoization to avoid redundant computations.

#### Solution:

```python
def longestIncreasingPath(matrix):
    if not matrix or not matrix[0]:
        return 0
  
    m, n = len(matrix), len(matrix[0])
    memo = [[-1] * n for _ in range(m)]
  
    def dfs(i, j):
        if memo[i][j] != -1:
            return memo[i][j]
      
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        max_path = 1
      
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > matrix[i][j]:
                max_path = max(max_path, 1 + dfs(ni, nj))
      
        memo[i][j] = max_path
        return max_path
  
    return max(dfs(i, j) for i in range(m) for j in range(n))

# Example test case
matrix = [
  [9, 9, 4],
  [6, 6, 8],
  [2, 1, 1]
]
print(longestIncreasingPath(matrix))  # Output: 4
```

#### Time and Space Complexity:

```python
# Time Complexity: O(m * n), where m is the number of rows and n is the number of columns.
# Each cell is visited only once due to memoization.

# Space Complexity: O(m * n), because we use a memo array to store the results of each cell.
```

#### Alternative Approach:

There is no significantly different alternative approach that would improve the time complexity, as DFS with memoization is already optimal for this type of problem.

---

### 8. **Distinct Subsequences** (Hard)

#### Problem Explanation:

Given two strings `s` and `t`, return the number of distinct subsequences of `s` that equal `t`. A subsequence is a sequence derived from another string by deleting some or no characters without changing the order of the remaining characters.

#### Numeric Example:

```
Input: s = "rabbbit", t = "rabbit"
Output: 3

Explanation:
There are 3 distinct ways to form "rabbit" from "rabbbit":
1. "rabbbit" → remove the first 'b'
2. "rabbbit" → remove the second 'b'
3. "rabbbit" → remove the third 'b'
```

#### Coding Pattern:

This problem can be solved using **Dynamic Programming**. We define a 2D `dp` array where `dp[i][j]` represents the number of distinct subsequences of `s[0:i]` that match `t[0:j]`. The recurrence relation is:

```
dp[i][j] = dp[i-1][j] + dp[i-1][j-1] if s[i-1] == t[j-1]
else dp[i][j] = dp[i-1][j]
```

#### Solution:

```python
def numDistinct(s, t):
    m, n = len(s), len(t)
  
    # Step 1: Initialize a dp array of size (m+1) x (n+1)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
  
    # Step 2: If t is an empty string, there is exactly one subsequence that matches (the empty subsequence)
    for i in range(m + 1):
        dp[i][0] = 1
  
    # Step 3: Fill the dp array
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
            else:
                dp[i][j] = dp[i

 - 1][j]
  
    return dp[m][n]

# Example test case
s = "rabbbit"
t = "rabbit"
print(numDistinct(s, t))  # Output: 3
```

#### Time and Space Complexity:

```python
# Time Complexity: O(m * n), where m is the length of s and n is the length of t.
# We fill a 2D dp array of size (m+1) x (n+1).

# Space Complexity: O(m * n), because we use a 2D array to store the number of distinct subsequences.
```

#### Alternative Approach:

The space complexity can be optimized to `O(n)` by only maintaining the current and previous rows of the `dp` array.

Here’s the space-optimized approach:

```python
def numDistinct(s, t):
    m, n = len(s), len(t)
  
    dp = [0] * (n + 1)
    dp[0] = 1  # Base case: an empty t can be formed by an empty s
  
    for i in range(1, m + 1):
        prev = dp[:]  # Make a copy of the previous dp state
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                dp[j] = prev[j] + prev[j - 1]
            else:
                dp[j] = prev[j]
  
    return dp[n]

# Example test case
s = "rabbbit"
t = "rabbit"
print(numDistinct(s, t))  # Output: 3
```

---

Let's continue with the next set of problems from the **2-D Dynamic Programming** section.

---

### 9. **Edit Distance** (Medium)

#### Problem Explanation:

Given two strings `word1` and `word2`, return the minimum number of operations required to convert `word1` to `word2`. You have three operations available:

1. Insert a character.
2. Delete a character.
3. Replace a character.

#### Numeric Example:

```
Input: word1 = "horse", word2 = "ros"
Output: 3

Explanation:
- Replace 'h' with 'r'
- Remove 'o'
- Remove 'e'
```

#### Coding Pattern:

This problem can be solved using **Dynamic Programming**. We define a 2D `dp` array where `dp[i][j]` represents the minimum number of operations required to convert `word1[0:i]` to `word2[0:j]`. The recurrence relation is:

```
if word1[i-1] == word2[j-1]:
    dp[i][j] = dp[i-1][j-1]
else:
    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
```

This relation covers three cases:

- `dp[i-1][j]` → delete from `word1`.
- `dp[i][j-1]` → insert into `word1`.
- `dp[i-1][j-1]` → replace in `word1`.

#### Solution:

```python
def minDistance(word1, word2):
    m, n = len(word1), len(word2)
  
    # Step 1: Initialize a dp array with dimensions (m+1) x (n+1)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
  
    # Step 2: Fill the base cases for transforming an empty string to any string
    for i in range(1, m + 1):
        dp[i][0] = i
    for j in range(1, n + 1):
        dp[0][j] = j
  
    # Step 3: Fill the dp array using the recurrence relation
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
  
    return dp[m][n]

# Example test case
word1 = "horse"
word2 = "ros"
print(minDistance(word1, word2))  # Output: 3
```

#### Time and Space Complexity:

```python
# Time Complexity: O(m * n), where m is the length of word1 and n is the length of word2.
# We fill a 2D array of size (m+1) x (n+1).

# Space Complexity: O(m * n), because we use a 2D array to store the minimum operations for each substring.
```

#### Alternative Approach:

The space complexity can be optimized to `O(n)` by only maintaining the current and previous rows of the `dp` array, as we only need the previous row to compute the current row.

Here’s the space-optimized approach:

```python
def minDistance(word1, word2):
    m, n = len(word1), len(word2)
  
    dp = [0] * (n + 1)
  
    # Step 1: Initialize the base case
    for j in range(1, n + 1):
        dp[j] = j
  
    # Step 2: Fill the dp array row by row
    for i in range(1, m + 1):
        prev = dp[:]  # Copy the current dp state
        dp[0] = i  # Base case: transforming from word1[0:i] to an empty string
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[j] = prev[j - 1]
            else:
                dp[j] = 1 + min(prev[j], dp[j - 1], prev[j - 1])
  
    return dp[n]

# Example test case
word1 = "horse"
word2 = "ros"
print(minDistance(word1, word2))  # Output: 3
```

---

### 10. **Burst Balloons** (Hard)

#### Problem Explanation:

You are given `n` balloons, indexed from 0 to `n - 1`. Each balloon has a number printed on it. You are asked to burst all the balloons. If you burst the `i`-th balloon, you will get `nums[left] * nums[i] * nums[right]` coins. The left and right neighbors are considered for the next steps. Your task is to find the maximum number of coins you can collect by bursting the balloons wisely.

#### Numeric Example:

```
Input: nums = [3, 1, 5, 8]
Output: 167

Explanation:
By bursting balloons in the order of [1, 5, 8, 3], you get the maximum coins.
```

#### Coding Pattern:

This problem can be solved using **Dynamic Programming** with a bottom-up approach. We define `dp[left][right]` as the maximum coins we can get by bursting balloons between `left` and `right`. The idea is to consider each balloon `k` between `left` and `right` as the last balloon to burst in that range and compute the coins from bursting it.

#### Solution:

```python
def maxCoins(nums):
    # Step 1: Add virtual balloons with value 1 at both ends
    nums = [1] + nums + [1]
    n = len(nums)
  
    # Step 2: Initialize the dp array
    dp = [[0] * n for _ in range(n)]
  
    # Step 3: Fill the dp array using a bottom-up approach
    for length in range(2, n):  # length is the distance between left and right boundaries
        for left in range(0, n - length):
            right = left + length
            for k in range(left + 1, right):
                dp[left][right] = max(dp[left][right], dp[left][k] + dp[k][right] + nums[left] * nums[k] * nums[right])
  
    return dp[0][n - 1]

# Example test case
nums = [3, 1, 5, 8]
print(maxCoins(nums))  # Output: 167
```

#### Time and Space Complexity:

```python
# Time Complexity: O(n^3), where n is the length of the nums array.
# We fill a 2D array and for each subproblem, we iterate through all possible middle points.

# Space Complexity: O(n^2), because we use a 2D array to store the maximum coins for each subarray.
```

#### Alternative Approach:

There is no significantly different alternative approach. Dynamic Programming is the optimal solution for this problem due to its overlapping subproblems and optimal substructure properties.

---

### 11. **Regular Expression Matching** (Hard)

#### Problem Explanation:

Given an input string `s` and a pattern `p`, implement regular expression matching with support for `.` and `*`.

- `.` matches any single character.
- `*` matches zero or more of the preceding element.

The matching should cover the entire input string, not partial matches.

#### Numeric Example:

```
Input: s = "aab", p = "c*a*b"
Output: true

Explanation:
The pattern "c*a*b" can match "aab" because "c*" can be ignored, "a*" matches "aa", and "b" matches "b".
```

#### Coding Pattern:

This problem can be solved using **Dynamic Programming**. We define a 2D `dp` array where `dp[i][j]` indicates whether `s[0:i]` matches `p[0:j]`. The key cases are:

- If `p[j-1] == s[i-1]` or `p[j-1] == '.'`, then `dp[i][j] = dp[i-1][j-1]`.
- If `p[j-1] == '*'`, we have two options:
  - If `p[j-2]` is ignored: `dp[i][j] = dp[i][j-2]`.
  - If `p[j-2] == s[i-1]` or `p[j-2] == '.'`, then `dp[i][j] = dp[i-1][j]`.

#### Solution:

```python
def isMatch(s, p):
    m, n = len(s), len(p)
  
    # Step 1: Initialize the dp array with dimensions (m+1) x (n+1)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True  # Empty string matches an empty pattern
  
    # Step 2: Handle patterns with '*' at the start (they can match an empty string)
    for j in range(2, n + 1):
        if p

[j - 1] == '*':
            dp[0][j] = dp[0][j - 2]
  
    # Step 3: Fill the dp array
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                dp[i][j] = dp[i][j - 2]  # '*' matches zero occurrences
                if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                    dp[i][j] = dp[i][j] or dp[i - 1][j]  # '*' matches one or more occurrences
  
    return dp[m][n]

# Example test case
s = "aab"
p = "c*a*b"
print(isMatch(s, p))  # Output: True
```

#### Time and Space Complexity:

```python
# Time Complexity: O(m * n), where m is the length of s and n is the length of p.
# We fill a 2D array of size (m+1) x (n+1).

# Space Complexity: O(m * n), because we use a 2D array to store the match results for each substring combination.
```

#### Alternative Approach:

There is no fundamentally different approach. The **Dynamic Programming** method is the optimal solution for this problem.

---

Let's now move on to the **Greedy** section, continuing from the first problem listed.

---

## Greedy

### 1. **Maximum Subarray** (Medium)

#### Problem Explanation:

Given an integer array `nums`, find the contiguous subarray (containing at least one number) that has the largest sum and return its sum.

#### Numeric Example:

```
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6

Explanation:
The subarray [4,-1,2,1] has the largest sum = 6.
```

#### Coding Pattern:

This problem can be solved using **Greedy** and **Kadane’s Algorithm**. We maintain a running sum and reset it to 0 if it becomes negative. At each step, we update the maximum sum.

#### Solution:

```python
def maxSubArray(nums):
    # Step 1: Initialize variables for the current sum and maximum sum
    current_sum = max_sum = nums[0]
  
    # Step 2: Iterate through the array
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)  # Either extend the current subarray or start a new one
        max_sum = max(max_sum, current_sum)  # Update the maximum sum
  
    return max_sum

# Example test case
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))  # Output: 6
```

#### Time and Space Complexity:

```python
# Time Complexity: O(n), where n is the length of the input array.
# We traverse the array once.

# Space Complexity: O(1), because we only use a few variables to keep track of the current and maximum sum.
```

#### Alternative Approach:

This problem is most optimally solved using **Kadane’s Algorithm**, which is already `O(n)` in time complexity and `O(1)` in space complexity. There is no more efficient approach.

---

### 2. **Jump Game** (Medium)

#### Problem Explanation:

Given an array of non-negative integers `nums`, where each element represents your maximum jump length at that position, determine if you are able to reach the last index.

#### Numeric Example:

```
Input: nums = [2,3,1,1,4]
Output: true

Explanation:
Start at index 0. You can jump 1 step to index 1, then 3 steps to the last index.
```

#### Coding Pattern:

This problem can be solved using **Greedy**. We maintain a variable `farthest` to track the farthest index we can reach. As we iterate through the array, we update `farthest` based on the current index and the maximum jump possible from that index.

#### Solution:

```python
def canJump(nums):
    farthest = 0
  
    # Step 1: Iterate through the array and update the farthest index we can reach
    for i in range(len(nums)):
        if i > farthest:  # If we can't reach index i, return False
            return False
        farthest = max(farthest, i + nums[i])  # Update the farthest index we can reach
  
    return True  # If we complete the loop, it means we can reach the last index

# Example test case
nums = [2, 3, 1, 1, 4]
print(canJump(nums))  # Output: True
```

#### Time and Space Complexity:

```python
# Time Complexity: O(n), where n is the length of the input array.
# We traverse the array once to check if we can reach the last index.

# Space Complexity: O(1), because we only use a few variables to track the farthest index.
```

#### Alternative Approach:

There is no fundamentally different approach that improves upon this greedy solution. It is already optimal in terms of time and space complexity.

---

### 3. **Jump Game II** (Medium)

#### Problem Explanation:

Given an array of non-negative integers `nums`, where each element represents your maximum jump length at that position, return the minimum number of jumps needed to reach the last index.

#### Numeric Example:

```
Input: nums = [2,3,1,1,4]
Output: 2

Explanation:
The minimum number of jumps is 2. Jump 1 step from index 0 to index 1, then 3 steps to the last index.
```

#### Coding Pattern:

This problem can also be solved using **Greedy**. We maintain a `farthest` variable to track how far we can reach, and a `jumps` counter to count how many jumps we need. Whenever we reach the end of the current range, we increase the jump count and update the range.

#### Solution:

```python
def jump(nums):
    jumps = 0
    farthest = 0
    current_end = 0
  
    # Step 1: Iterate through the array (but we don't need to check the last element)
    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])  # Update the farthest we can reach
      
        # Step 2: If we've reached the end of the current range, we need to make a jump
        if i == current_end:
            jumps += 1
            current_end = farthest  # Update the current range to the farthest index we can reach
  
    return jumps

# Example test case
nums = [2, 3, 1, 1, 4]
print(jump(nums))  # Output: 2
```

#### Time and Space Complexity:

```python
# Time Complexity: O(n), where n is the length of the input array.
# We traverse the array once, updating the farthest point we can reach at each step.

# Space Complexity: O(1), because we only use a few variables to track the farthest point, current range, and jump count.
```

#### Alternative Approach:

This greedy approach is optimal and solves the problem with the minimum number of jumps in `O(n)` time and `O(1)` space. There is no more efficient approach.

---

### 4. **Gas Station** (Medium)

#### Problem Explanation:

There are `n` gas stations along a circular route, where the amount of gas at station `i` is `gas[i]`. You have a car with an unlimited gas tank, but it costs `cost[i]` of gas to travel from station `i` to station `i + 1`. You begin the journey with an empty tank at one of the gas stations. Return the starting gas station index if you can complete the circuit once, otherwise return `-1`.

#### Numeric Example:

```
Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3

Explanation:
Start at station 3 (index 3), and you can complete the circuit.
```

#### Coding Pattern:

This problem can be solved using **Greedy**. We need to check if the total gas is greater than or equal to the total cost. If it is, then we can complete the circuit. While traversing the gas stations, we keep track of the current tank of gas. If at any point the current tank becomes negative, we reset the starting station to the next one.

#### Solution:

```python
def canCompleteCircuit(gas, cost):
    total_tank, current_tank = 0, 0
    start_station = 0
  
    # Step 1: Iterate through all gas stations
    for i in range(len(gas)):
        total_tank += gas[i] - cost[i]
        current_tank += gas[i] - cost[i]
      
        # Step 2: If current tank is negative, we can't start from this station, reset start station
        if current_tank < 0:
            start_station = i + 1
            current_tank = 0
  
    # Step 3: If total gas is less than total cost, return -1, otherwise return the starting station
    return start_station if total_tank >= 0 else -1

# Example test case
gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
print(canCompleteCircuit(gas, cost))  # Output: 3
```

#### Time and Space Complexity:

```python
# Time Complexity: O(n), where n is the number of gas stations.
# We traverse the list of gas stations once, updating the tank at each step.

# Space Complexity: O(1), because we only use a few variables to track the total tank, current tank, and starting station.
```

#### Alternative Approach:

This greedy approach is optimal, solving the problem in linear time with constant space. There is no need for a more complex approach, as this is the most efficient.

---

Let's continue with the remaining problems from the **Greedy** section.

---

### 5. **Hand of Straights** (Medium)

#### Problem Explanation:

You are given an array of integers `hand`, where `hand[i]` represents the number of a card, and an integer `groupSize`. The task is to determine if you can rearrange the cards into groups of `groupSize`, where each group consists of consecutive cards.

#### Numeric Example:

```
Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
Output: true

Explanation:
You can rearrange the cards into groups of 3: [1,2,3], [2,3,4], [6,7,8].
```

#### Coding Pattern:

This problem can be solved using a **Greedy** approach. The idea is to always try to form a group starting with the smallest available card. We use a frequency map to count the occurrences of each card and reduce the count as we form valid groups.

#### Solution:

```python
from collections import Counter

def isNStraightHand(hand, groupSize):
    if len(hand) % groupSize != 0:
        return False
  
    # Step 1: Count the occurrences of each card
    card_count = Counter(hand)
  
    # Step 2: Iterate through the sorted cards and try to form groups
    for card in sorted(card_count):
        if card_count[card] > 0:
            for i in range(groupSize):
                if card_count[card + i] < card_count[card]:
                    return False
                card_count[card + i] -= card_count[card]
  
    return True

# Example test case
hand = [1, 2, 3, 6, 2, 3, 4, 7, 8]
groupSize = 3
print(isNStraightHand(hand, groupSize))  # Output: True
```

#### Time and Space Complexity:

```python
# Time Complexity: O(n log n), where n is the number of cards in the hand.
# Sorting the hand takes O(n log n), and iterating over the cards takes O(n).

# Space Complexity: O(n), because we use a frequency map to store the count of each card.
```

#### Alternative Approach:

There is no fundamentally different approach, as the greedy solution with a frequency map is optimal in terms of time complexity. Sorting is necessary to ensure that consecutive groups are formed.

---

### 6. **Merge Triplets to Form Target Triplet** (Medium)

#### Problem Explanation:

You are given a list of triplets `triplets`, where `triplets[i] = [ai, bi, ci]` describes the values of the `i-th` triplet. You are also given a target triplet `target = [x, y, z]`. The task is to check if it is possible to pick some triplets from the list and merge them to form the target triplet. Merging two triplets means taking the maximum value from each position.

#### Numeric Example:

```
Input: triplets = [[2,5,3], [1,8,4], [1,7,5]], target = [2,7,5]
Output: true

Explanation:
- Select the triplet [2,5,3] and [1,7,5].
- Merge them: max(2,1) = 2, max(5,7) = 7, max(3,5) = 5 → The result is [2,7,5].
```

#### Coding Pattern:

We can solve this using a **Greedy** approach. We try to merge triplets that are component-wise less than or equal to the target triplet. For each valid triplet, we update a result array that tracks the maximum values seen so far. At the end, we check if the result matches the target.

#### Solution:

```python
def mergeTriplets(triplets, target):
    result = [0, 0, 0]
  
    # Step 1: Iterate through the triplets
    for triplet in triplets:
        if triplet[0] <= target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]:
            result = [max(result[i], triplet[i]) for i in range(3)]
  
    # Step 2: Check if the result matches the target
    return result == target

# Example test case
triplets = [[2, 5, 3], [1, 8, 4], [1, 7, 5]]
target = [2, 7, 5]
print(mergeTriplets(triplets, target))  # Output: True
```

#### Time and Space Complexity:

```python
# Time Complexity: O(n), where n is the number of triplets in the list.
# We iterate through the list once and update the result array.

# Space Complexity: O(1), because we only use a fixed-size result array.
```

#### Alternative Approach:

There is no more efficient approach for this problem. The greedy approach of selecting triplets that are less than or equal to the target in all components is optimal.

---

### 7. **Partition Labels** (Medium)

#### Problem Explanation:

You are given a string `s`. The task is to partition the string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

#### Numeric Example:

```
Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]

Explanation:
- The first partition is "ababcbaca", the second is "defegde", and the third is "hijhklij".
- Each letter appears in at most one part.
```

#### Coding Pattern:

This problem can be solved using a **Greedy** approach. We first find the last occurrence of each character in the string. Then, we iterate through the string, maintaining the farthest point we can reach for the current partition. When the current index reaches this farthest point, we record the size of the partition and start a new one.

#### Solution:

```python
def partitionLabels(s):
    # Step 1: Record the last occurrence of each character
    last_occurrence = {char: i for i, char in enumerate(s)}
  
    result = []
    start, end = 0, 0
  
    # Step 2: Iterate through the string
    for i, char in enumerate(s):
        end = max(end, last_occurrence[char])  # Extend the current partition to the farthest last occurrence
      
        # Step 3: If we reach the end of the partition, record its size
        if i == end:
            result.append(i - start + 1)
            start = i + 1  # Start a new partition
  
    return result

# Example test case
s = "ababcbacadefegdehijhklij"
print(partitionLabels(s))  # Output: [9, 7, 8]
```

#### Time and Space Complexity:

```python
# Time Complexity: O(n), where n is the length of the string.
# We traverse the string twice: once to record the last occurrence of each character, and once to determine the partitions.

# Space Complexity: O(1), because we only use a fixed-size map to store the last occurrences of characters.
```

#### Alternative Approach:

This greedy approach is optimal, and there is no better method. The key observation is to form the partitions based on the last occurrences of characters.

---

### 8. **Valid Parenthesis String** (Medium)

#### Problem Explanation:

Given a string `s` containing only three types of characters: `'('`, `')'`, and `'*'`, return `True` if the string is valid. The string is considered valid if it can be turned into a valid parenthesis string by replacing each '*' with either `'('`, `')'`, or an empty string.

#### Numeric Example:

```
Input: s = "(*))"
Output: true

Explanation:
The string can be made valid by replacing '*' with an empty string.
```

#### Coding Pattern:

This problem can be solved using a **Greedy** approach. We maintain two counts: `low` (the minimum possible open parentheses) and `high` (the maximum possible open parentheses). For each character:

- If it’s `'('`, both `low` and `high` are incremented.
- If it’s `')'`, both are decremented.
- If it’s `'*'`, we consider it can be either `'('`, `')'`, or an empty string, so `low` is decremented, and `high` is incremented.
  Finally, if `low` is 0, it means that there is a valid sequence of parentheses.

#### Solution:

```python
def checkValidString(s):
    low = 0  # Minimum possible open parentheses
    high = 0  # Maximum possible open parentheses
  
    # Step 1: Iterate through the string
    for char in s:
        if char == '(':
            low += 1
            high += 1
        elif char == ')':
            low -= 1
            high -= 1
        else:  # char == '*'
            low -= 1  # Consider '*' as ')'
            high += 1  # Consider '*' as '('
      
        # Step 2: Ensure low does not drop below 0
        if high < 0:  # Too many

 closing parentheses
            return False
        low = max(low, 0)
  
    return low == 0

# Example test case
s = "(*))"
print(checkValidString(s))  # Output: True
```

#### Time and Space Complexity:

```python
# Time Complexity: O(n), where n is the length of the string.
# We traverse the string once, updating the counts at each step.

# Space Complexity: O(1), because we only use a few variables to track the possible number of open parentheses.
```

#### Alternative Approach:

This greedy approach is optimal, solving the problem in `O(n)` time with `O(1)` space complexity. There is no more efficient approach.

---

## **INTERVALS**

### 1. **Insert Interval** (Medium)

#### Problem Explanation:

You are given an array of non-overlapping intervals `intervals` where `intervals[i] = [start_i, end_i]` represent the start and end of the `i-th` interval, and the intervals are sorted in ascending order by `start_i`. You are also given a new interval `newInterval = [start, end]` that you need to insert into the intervals. The resulting intervals should still be non-overlapping and sorted in ascending order.

#### Numeric Example:

```
Input: intervals = [[1,3], [6,9]], newInterval = [2,5]
Output: [[1,5], [6,9]]

Explanation:
- The interval [2, 5] overlaps with [1, 3]. We merge them to form [1, 5].
- The resulting intervals are [[1, 5], [6, 9]].
```

#### Coding Pattern:

This problem can be solved using an **Interval Merging** pattern. The key steps are:

1. Iterate through the intervals and add all intervals that come before the `newInterval` (i.e., intervals that do not overlap with it).
2. Merge all intervals that overlap with `newInterval`.
3. Add all remaining intervals that come after the `newInterval`.

#### Solution:

```python
def insert(intervals, newInterval):
    result = []
    i = 0
    n = len(intervals)
  
    # Step 1: Add all intervals that end before the new interval starts (no overlap).
    while i < n and intervals[i][1] < newInterval[0]:
        result.append(intervals[i])
        i += 1
  
    # Step 2: Merge all intervals that overlap with the new interval.
    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])  # Adjust start to the smallest
        newInterval[1] = max(newInterval[1], intervals[i][1])  # Adjust end to the largest
        i += 1
  
    # Add the merged interval to the result.
    result.append(newInterval)
  
    # Step 3: Add the remaining intervals that start after the new interval ends.
    while i < n:
        result.append(intervals[i])
        i += 1
  
    return result

# Example test case
intervals = [[1, 3], [6, 9]]
newInterval = [2, 5]
print(insert(intervals, newInterval))  # Output: [[1, 5], [6, 9]]
```

#### Time and Space Complexity:

```python
# Time Complexity: O(n), where n is the number of intervals.
# We iterate through all the intervals exactly once to either add or merge them.

# Space Complexity: O(n), where n is the number of intervals.
# We store the result in a list of intervals, which takes linear space.
```

#### Alternative Approach:

There is no significantly better alternative approach, as the greedy solution efficiently handles interval merging in a single pass through the list. Here’s a more detailed step-by-step explanation with comments.

---

### 2. **Merge Intervals** (Medium)

#### Problem Explanation:

Given an array of intervals where `intervals[i] = [start_i, end_i]`, merge all overlapping intervals and return an array of the non-overlapping intervals that cover all the intervals in the input.

#### Numeric Example:

```
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]

Explanation:
- Intervals [1,3] and [2,6] overlap, so we merge them into [1,6].
- The other intervals do not overlap, so they remain as they are.
```

#### Coding Pattern:

This problem can also be solved using the **Interval Merging** pattern. The key steps are:

1. Sort the intervals by their start time.
2. Iterate through the sorted intervals and merge any overlapping intervals.

#### Solution:

```python
def merge(intervals):
    # Step 1: Sort intervals by their start times.
    intervals.sort(key=lambda x: x[0])
  
    result = []
  
    # Step 2: Iterate through intervals and merge overlapping ones.
    for interval in intervals:
        # If result is empty or the current interval does not overlap with the last one, add it.
        if not result or result[-1][1] < interval[0]:
            result.append(interval)
        else:
            # Merge the current interval with the last interval in result.
            result[-1][1] = max(result[-1][1], interval[1])
  
    return result

# Example test case
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge(intervals))  # Output: [[1, 6], [8, 10], [15, 18]]
```

#### Time and Space Complexity:

```python
# Time Complexity: O(n log n), where n is the number of intervals.
# Sorting the intervals takes O(n log n), and iterating through them takes O(n).

# Space Complexity: O(n), where n is the number of intervals.
# We store the merged intervals in a result list, which takes linear space.
```

#### Alternative Approach:

The greedy interval merging approach is optimal and commonly used for interval problems. We could use a divide-and-conquer approach, but the complexity would still involve sorting, so the overall time complexity remains O(n log n).

---

### 3. **Non-overlapping Intervals** (Medium)

#### Problem Explanation:

Given an array of intervals `intervals` where `intervals[i] = [start_i, end_i]`, return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

#### Numeric Example:

```
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1

Explanation:
- We remove the interval [1, 3] to make the rest of the intervals non-overlapping.
```

#### Coding Pattern:

This problem can be solved using **Greedy**. We can sort the intervals by their end time and then iterate through the intervals, counting how many intervals need to be removed to ensure no overlap.

#### Solution:

```python
def eraseOverlapIntervals(intervals):
    # Step 1: Sort intervals by their end times.
    intervals.sort(key=lambda x: x[1])
  
    count = 0
    prev_end = float('-inf')
  
    # Step 2: Iterate through intervals and count overlapping intervals.
    for start, end in intervals:
        if start >= prev_end:
            # No overlap, update prev_end.
            prev_end = end
        else:
            # Overlapping, increment count.
            count += 1
  
    return count

# Example test case
intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
print(eraseOverlapIntervals(intervals))  # Output: 1
```

#### Time and Space Complexity:

```python
# Time Complexity: O(n log n), where n is the number of intervals.
# Sorting the intervals takes O(n log n), and iterating through them takes O(n).

# Space Complexity: O(1), since we are only using a few extra variables.
```

#### Alternative Approach:

This greedy approach is optimal for minimizing the number of intervals removed. There’s no better solution in terms of time or space complexity.

---

### 4. **Meeting Rooms** (Easy)

#### Problem Explanation:

Given an array of meeting time intervals `intervals` where `intervals[i] = [start_i, end_i]`, determine if a person can attend all meetings. If no intervals overlap, return `True`, otherwise return `False`.

#### Numeric Example:

```
Input: intervals = [[0,30],[5,10],[15,20]]
Output: false

Explanation:
- The meeting [0, 30] overlaps with [5, 10], so it's not possible to attend all meetings.
```

#### Coding Pattern:

This problem can be solved using **Greedy**. We sort the intervals by their start time and check if any two consecutive intervals overlap.

#### Solution:

```python
def canAttendMeetings(intervals):
    # Step 1: Sort intervals by their start time.
    intervals.sort(key=lambda x: x[0])
  
    # Step 2: Check for overlapping intervals.
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:
            return False  # Overlap found
  
    return True

# Example test case
intervals = [[0, 30], [5, 10], [15, 20]]
print(canAttendMeetings(intervals))  # Output: False
```

#### Time and Space Complexity:

```python
# Time Complexity: O(n log n), where n is the number of intervals.
# Sorting the intervals takes O(n log n), and checking for overlap takes O(n).

# Space Complexity: O(1), since we only use a few variables.
```

#### Alternative Approach:

The greedy approach of sorting and checking for overlaps is optimal. There’s no faster way to determine if all meetings can be attended.

---

### 5. **Meeting Rooms II** (Medium)

#### Problem Explanation:

Given an array of meeting time intervals `intervals` where `intervals[i] = [start_i, end_i]`, return the minimum number of conference rooms required.

#### Numeric Example:

```
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2

Explanation:
- Two meetings overlap, so at least two conference rooms are required.
```

#### Coding Pattern:

This problem can be solved using a **Greedy + Two Pointers** approach. We track the start and end times of meetings and determine the minimum number of overlapping intervals using a two-pointer technique.

#### Solution:

```python
def minMeetingRooms(intervals):
    if not intervals:
        return 0
  
    # Step 1: Extract start and end times, and sort them separately.
    start_times = sorted([interval[0] for interval in intervals])
    end_times = sorted([interval[1] for interval in intervals])
  
    start_ptr, end_ptr = 0, 0
    rooms_needed, max_rooms = 0, 0
  
    # Step 2: Use two pointers to track the number of overlapping meetings.
    while start_ptr < len(intervals):
        if start_times[start_ptr] < end_times[end_ptr]:
            rooms_needed += 1
            start_ptr += 1
        else:
            rooms_needed -= 1
            end_ptr += 1
        max_rooms = max(max_rooms, rooms_needed)
  
    return max_rooms

# Example test case
intervals = [[0, 30], [5, 10], [15, 20]]
print(minMeetingRooms(intervals))  # Output: 2
```

#### Time and Space Complexity:

```python
# Time Complexity: O(n log n), where n is the number of intervals.
# Sorting the start and end times takes O(n log n), and the two-pointer technique takes O(n).

# Space Complexity: O(n), because we store the start and end times in two separate lists.
```

#### Alternative Approach:

The two-pointer technique is optimal for minimizing the number of conference rooms. Another approach could involve using a priority queue to track ongoing meetings, but the time complexity would remain the same.

---

Let's continue with the remaining problems from the **Intervals** section and then move on to the **Math & Geometry** and **Bit Manipulation** sections.

---

### 6. **Minimum Interval to Include Each Query** (Hard)

#### Problem Explanation:

You are given an array of intervals `intervals`, where `intervals[i] = [start_i, end_i]` represent the start and end of the `i-th` interval. You are also given an array of queries `queries`, where each query represents a point. For each query, find the minimum size of an interval from the list of intervals that includes the query point. If no interval contains the query, return `-1`.

#### Numeric Example:

```
Input: intervals = [[1, 4], [2, 4], [3, 6], [4, 4]], queries = [2, 3, 4, 5]
Output: [3, 3, 1, 4]

Explanation:
- For query 2, the smallest interval that includes it is [1, 4] or [2, 4] (size 3).
- For query 3, the smallest interval that includes it is [2, 4] or [3, 6] (size 3).
- For query 4, the smallest interval is [4, 4] (size 1).
- For query 5, the smallest interval is [3, 6] (size 4).
```

#### Coding Pattern:

This problem can be efficiently solved using a **Greedy + Sorting** technique. The idea is to first sort both intervals and queries. Then, for each query, maintain a list of intervals that include the query, and remove any intervals that no longer apply. A min-heap can help us efficiently find the smallest interval that contains each query.

#### Solution:

```python
import heapq

def minInterval(intervals, queries):
    # Step 1: Sort intervals by their start time
    intervals.sort()
    # Step 2: Sort queries and store the original indices to return results in order
    sorted_queries = sorted((q, i) for i, q in enumerate(queries))
  
    result = [-1] * len(queries)  # To store results in the original query order
    min_heap = []  # Min-heap to track intervals that can cover the query
    i = 0  # Pointer for intervals
  
    # Step 3: Process each query
    for query, index in sorted_queries:
        # Add all intervals that can start before or at the current query
        while i < len(intervals) and intervals[i][0] <= query:
            start, end = intervals[i]
            # If the interval can cover the query, add it to the heap
            if end >= query:
                heapq.heappush(min_heap, (end - start + 1, end))  # Store the interval length and end time
            i += 1
      
        # Remove intervals that end before the query
        while min_heap and min_heap[0][1] < query:
            heapq.heappop(min_heap)
      
        # The smallest valid interval is at the top of the heap
        if min_heap:
            result[index] = min_heap[0][0]
  
    return result

# Example test case
intervals = [[1, 4], [2, 4], [3, 6], [4, 4]]
queries = [2, 3, 4, 5]
print(minInterval(intervals, queries))  # Output: [3, 3, 1, 4]
```

#### Time and Space Complexity:

```python
# Time Complexity: O((n + m) log n), where n is the number of intervals and m is the number of queries.
# Sorting the intervals takes O(n log n), sorting the queries takes O(m log m), and we process each query in O(log n).

# Space Complexity: O(n), where n is the number of intervals stored in the min-heap at any point.
```

#### Alternative Approach:

This greedy approach combined with a min-heap is efficient for minimizing the interval size. Other approaches, such as using brute force to check all intervals for each query, would result in O(n * m) complexity, which is much slower.

---

## Math & Geometry

### 7. **Rotate Image** (Medium)

#### Problem Explanation:

You are given an `n x n` 2D matrix representing an image. Rotate the image by 90 degrees (clockwise) in-place, meaning you cannot use extra space for another matrix.

#### Numeric Example:

```
Input: matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
Output: [
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
```

#### Coding Pattern:

This problem can be solved using a **Matrix Rotation** pattern. First, transpose the matrix (convert rows to columns), and then reverse each row to achieve a 90-degree clockwise rotation.

#### Solution:

```python
def rotate(matrix):
    n = len(matrix)
  
    # Step 1: Transpose the matrix (convert rows to columns)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
  
    # Step 2: Reverse each row to get the rotated matrix
    for i in range(n):
        matrix[i].reverse()

# Example test case
matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
rotate(matrix)
print(matrix)  # Output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
```

#### Time and Space Complexity:

```python
# Time Complexity: O(n^2), where n is the dimension of the matrix.
# We iterate through the matrix twice: once for the transpose and once for reversing the rows.

# Space Complexity: O(1), because we perform the rotation in place without using additional space.
```

#### Alternative Approach:

There is no fundamentally better approach than transposing and reversing the matrix. The solution efficiently performs the rotation in place with O(1) space complexity.

---

### 8. **Spiral Matrix** (Medium)

#### Problem Explanation:

Given an `m x n` matrix, return all elements of the matrix in spiral order.

#### Numeric Example:

```
Input: matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]
```

#### Coding Pattern:

This problem can be solved using a **Spiral Traversal** pattern. The key is to keep track of the boundaries of the matrix (top, bottom, left, right) and adjust these boundaries as we traverse in a spiral manner.

#### Solution:

```python
def spiralOrder(matrix):
    result = []
  
    # Step 1: Define the boundaries of the spiral
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
  
    # Step 2: Traverse the matrix in a spiral manner
    while top <= bottom and left <= right:
        # Traverse from left to right
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1
      
        # Traverse from top to bottom
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
      
        if top <= bottom:
            # Traverse from right to left
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
      
        if left <= right:
            # Traverse from bottom to top
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
  
    return result

# Example test case
matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
print(spiralOrder(matrix))  # Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]
```

#### Time and Space Complexity:

```python
# Time Complexity: O(m * n), where m is the number of rows and n is the number of columns.
# We visit each element of the matrix exactly once.

# Space Complexity: O(1), ignoring the space used for the result list, as we don't use any additional data structures.
```

#### Alternative Approach:

The spiral traversal pattern is optimal for this problem. Any alternative approach would involve traversing the matrix in some other order, but the time complexity would remain O(m * n).

---

Let's continue with the remaining problems from the **Math & Geometry** section and then move on to the **Bit Manipulation** section.

---

### 9. **Set Matrix Zeroes** (Medium)

#### Problem Explanation:

Given an `m x n` matrix, if an element is 0, set its entire row and column to 0. You must do this in place, without using extra space for another matrix.

#### Numeric Example:

```
Input: matrix = [
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: [
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
```

#### Coding Pattern:

This problem can be solved using the **Matrix Manipulation** pattern. We will use the first row and the first column as markers to store whether the entire row or column should be set to zero. Then, in a second pass, we update the matrix.

#### Solution:

```python
def setZeroes(matrix):
    # Step 1: Use the first row and first column as markers
    rows, cols = len(matrix), len(matrix[0])
    first_row_has_zero = any(matrix[0][j] == 0 for j in range(cols))
    first_col_has_zero = any(matrix[i][0] == 0 for i in range(rows))
  
    # Step 2: Mark the rows and columns that need to be set to zero
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][j] == 0:
                matrix[i][0] = 0  # Mark the row
                matrix[0][j] = 0  # Mark the column
  
    # Step 3: Zero out cells based on the markers
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
  
    # Step 4: Zero out the first row if needed
    if first_row_has_zero:
        for j in range(cols):
            matrix[0][j] = 0
  
    # Step 5: Zero out the first column if needed
    if first_col_has_zero:
        for i in range(rows):
            matrix[i][0] = 0

# Example test case
matrix = [
  [1, 1, 1],
  [1, 0, 1],
  [1, 1, 1]
]
setZeroes(matrix)
print(matrix)  # Output: [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
```

#### Time and Space Complexity:

```python
# Time Complexity: O(m * n), where m is the number of rows and n is the number of columns.
# We traverse the entire matrix twice: once to set markers and once to update the matrix.

# Space Complexity: O(1), because we are not using any extra space beyond the matrix itself.
```

#### Alternative Approach:

This in-place solution using the first row and column as markers is optimal. Using additional space (e.g., separate arrays to track rows and columns to zero) would increase space complexity to O(m + n).

---

### 10. **Happy Number** (Easy)

#### Problem Explanation:

Write an algorithm to determine if a number `n` is a happy number. A happy number is defined by repeatedly replacing the number with the sum of the squares of its digits until the number equals 1 (where it becomes happy) or it loops endlessly in a cycle that does not include 1.

#### Numeric Example:

```
Input: n = 19
Output: true

Explanation:
19 -> 1^2 + 9^2 = 82
82 -> 8^2 + 2^2 = 68
68 -> 6^2 + 8^2 = 100
100 -> 1^2 + 0^2 + 0^2 = 1 (happy)
```

#### Coding Pattern:

This problem can be solved using the **Cycle Detection** pattern. We can use Floyd's Cycle Detection Algorithm (also known as the tortoise and hare) to detect if the sequence enters a cycle.

#### Solution:

```python
def isHappy(n):
    def get_next(number):
        return sum(int(digit) ** 2 for digit in str(number))
  
    slow = n
    fast = get_next(n)
  
    # Step 1: Use the two-pointer technique to detect cycles
    while fast != 1 and slow != fast:
        slow = get_next(slow)
        fast = get_next(get_next(fast))
  
    return fast == 1

# Example test case
n = 19
print(isHappy(n))  # Output: True
```

#### Time and Space Complexity:

```python
# Time Complexity: O(log n), where n is the value of the number.
# Each step reduces the number of digits, and squaring each digit takes O(log n).

# Space Complexity: O(1), because we are using a constant amount of extra space (two pointers).
```

#### Alternative Approach:

An alternative approach is to use a set to track numbers we have seen before and detect cycles by checking if the number repeats. However, Floyd's Cycle Detection is more space-efficient with O(1) space.

---

### 11. **Plus One** (Easy)

#### Problem Explanation:

You are given a large integer represented as an array of digits. Increment the integer by one and return the resulting array of digits.

#### Numeric Example:

```
Input: digits = [1, 2, 9]
Output: [1, 3, 0]

Explanation:
- The number 129 is incremented to 130, so the output is [1, 3, 0].
```

#### Coding Pattern:

This problem can be solved using **Simple Arithmetic**. We start from the last digit and propagate any carry to the left.

#### Solution:

```python
def plusOne(digits):
    n = len(digits)
  
    # Step 1: Start from the last digit and propagate the carry
    for i in range(n - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
  
    # Step 2: If all digits were 9, we need to add an additional digit
    return [1] + digits

# Example test case
digits = [1, 2, 9]
print(plusOne(digits))  # Output: [1, 3, 0]
```

#### Time and Space Complexity:

```python
# Time Complexity: O(n), where n is the number of digits.
# We may need to traverse all digits in the worst case (e.g., [9, 9, 9]).

# Space Complexity: O(1), ignoring the output array (in-place modification of the input).
```

#### Alternative Approach:

The greedy approach of modifying digits from the least significant to the most significant digit is optimal. There are no faster methods to achieve this.

---

## Bit Manipulation

### 12. **Single Number** (Easy)

#### Problem Explanation:

Given a non-empty array of integers `nums`, every element appears twice except for one. Find that single element. Your algorithm should have a linear runtime complexity and use only constant extra space.

#### Numeric Example:

```
Input: nums = [4,1,2,1,2]
Output: 4

Explanation:
All elements except 4 appear twice, so 4 is the single number.
```

#### Coding Pattern:

This problem can be solved using **Bit Manipulation**. We can use the XOR operator (`^`), which cancels out any number that appears twice, leaving only the single number.

#### Solution:

```python
def singleNumber(nums):
    result = 0
    # Step 1: XOR all numbers. Pairs cancel each other, leaving the single number.
    for num in nums:
        result ^= num
    return result

# Example test case
nums = [4, 1, 2, 1, 2]
print(singleNumber(nums))  # Output: 4
```

#### Time and Space Complexity:

```python
# Time Complexity: O(n), where n is the length of the array.
# We iterate through the array once, performing XOR on each element.

# Space Complexity: O(1), since we are only using a constant amount of extra space (the result variable).
```

#### Alternative Approach:

This XOR approach is optimal for finding the single number in linear time and constant space. An alternative approach could involve using a set or hash map to track occurrences, but this would increase the space complexity to O(n).

---

### 13. **Number of 1 Bits** (Easy)

#### Problem Explanation:

Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

#### Numeric Example:

```
Input: n = 00000000000000000000000000001011
Output: 3

Explanation:
The binary representation of 11 has three '1' bits.
```

#### Coding Pattern:

This problem can be solved using **Bit Manipulation**. We can repeatedly shift the number right and count how many times the least significant bit is `1`.

#### Solution:

```python
def hammingWeight(n):
    count = 0


    # Step 1: Count the number of '1' bits in the binary representation of n
    while n:
        count += n & 1  # Check if the least significant bit is 1
        n >>= 1  # Right shift n by 1 to check the next bit
    return count

# Example test case
n = 0b00000000000000000000000000001011
print(hammingWeight(n))  # Output: 3
```

#### Time and Space Complexity:

```python
# Time Complexity: O(1), since n is a fixed 32-bit or 64-bit integer.
# The loop runs a fixed number of iterations (up to 32 or 64).

# Space Complexity: O(1), because we only use a few extra variables (count and n).
```

#### Alternative Approach:

An alternative approach is to repeatedly clear the least significant `1` bit using `n & (n - 1)`. This approach is slightly faster in cases where there are fewer `1` bits, but the overall complexity remains O(1).

---

Let’s continue with the remaining problems from the **Bit Manipulation** section.

---

### 14. **Counting Bits** (Easy)

#### Problem Explanation:

Given an integer `n`, return an array `ans` of length `n + 1` such that for each `i` (0 <= i <= n), `ans[i]` is the number of `1` bits in the binary representation of `i`.

#### Numeric Example:

```
Input: n = 5
Output: [0,1,1,2,1,2]

Explanation:
- 0 has 0 '1' bits.
- 1 has 1 '1' bit.
- 2 has 1 '1' bit.
- 3 has 2 '1' bits.
- 4 has 1 '1' bit.
- 5 has 2 '1' bits.
```

#### Coding Pattern:

This problem can be solved using a **Dynamic Programming + Bit Manipulation** pattern. The key observation is that the number of `1` bits in a number `i` can be related to the number of `1` bits in `i // 2` (right shift) plus the last bit (`i % 2`).

#### Solution:

```python
def countBits(n):
    # Step 1: Initialize the result array with 0 for all values
    dp = [0] * (n + 1)
  
    # Step 2: Fill the array using the relation dp[i] = dp[i >> 1] + (i & 1)
    for i in range(1, n + 1):
        dp[i] = dp[i >> 1] + (i & 1)
  
    return dp

# Example test case
n = 5
print(countBits(n))  # Output: [0, 1, 1, 2, 1, 2]
```

#### Time and Space Complexity:

```python
# Time Complexity: O(n), where n is the input integer.
# We iterate from 1 to n, filling the result array.

# Space Complexity: O(n), because we store the result in an array of size n + 1.
```

#### Alternative Approach:

This approach is optimal, using dynamic programming to compute the number of `1` bits in linear time. There’s no faster approach since we need to compute the bits for all numbers from `0` to `n`.

---

### 15. **Reverse Bits** (Easy)

#### Problem Explanation:

Reverse the bits of a given 32-bit unsigned integer.

#### Numeric Example:

```
Input: n = 43261596 (00000010100101000001111010011100 in binary)
Output: 964176192 (00111001011110000010100101000000 in binary)
```

#### Coding Pattern:

This problem can be solved using **Bit Manipulation**. We can reverse the bits by iterating over the 32 bits, shifting them into a new number.

#### Solution:

```python
def reverseBits(n):
    result = 0
  
    # Step 1: Iterate through all 32 bits
    for i in range(32):
        # Shift result to the left and add the current bit from n
        result = (result << 1) | (n & 1)
        n >>= 1  # Shift n to the right
  
    return result

# Example test case
n = 43261596  # In binary: 00000010100101000001111010011100
print(reverseBits(n))  # Output: 964176192 (00111001011110000010100101000000)
```

#### Time and Space Complexity:

```python
# Time Complexity: O(1), since we always perform exactly 32 iterations (constant number of bits).

# Space Complexity: O(1), as we only use a few extra variables (n and result).
```

#### Alternative Approach:

This approach is optimal for reversing the bits of a 32-bit integer. Using a different method (like bit shifts or masks) would result in the same complexity.

---

### 16. **Missing Number** (Easy)

#### Problem Explanation:

Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return the only number in the range that is missing from the array.

#### Numeric Example:

```
Input: nums = [3, 0, 1]
Output: 2

Explanation:
- The numbers in the range [0, 3] are {0, 1, 2, 3}.
- The number 2 is missing from the array.
```

#### Coding Pattern:

This problem can be solved using **Bit Manipulation** (XOR). The idea is that XORing all numbers from `0` to `n` with the numbers in the array will result in the missing number because all other numbers cancel out.

#### Solution:

```python
def missingNumber(nums):
    result = len(nums)
  
    # Step 1: XOR all indices and elements together
    for i in range(len(nums)):
        result ^= i ^ nums[i]
  
    return result

# Example test case
nums = [3, 0, 1]
print(missingNumber(nums))  # Output: 2
```

#### Time and Space Complexity:

```python
# Time Complexity: O(n), where n is the number of elements in the array.
# We iterate through the array once.

# Space Complexity: O(1), as we only use a constant amount of extra space (the result variable).
```

#### Alternative Approach:

An alternative approach is to use the sum formula for arithmetic sequences:

```
sum([0, 1, ..., n]) - sum(nums) = missing number
```

However, the XOR approach is preferable because it avoids potential integer overflow issues with very large numbers.

---

### 17. **Sum of Two Integers** (Medium)

#### Problem Explanation:

Given two integers `a` and `b`, return the sum of the two integers without using the operators `+` and `-`.

#### Numeric Example:

```
Input: a = 1, b = 2
Output: 3
```

#### Coding Pattern:

This problem can be solved using **Bit Manipulation** (using XOR for sum and AND for carry). The basic idea is that XOR (`^`) can sum bits without carry, while AND (`&`) followed by a left shift gives the carry.

#### Solution:

```python
def getSum(a, b):
    # Step 1: Repeat until there is no carry
    while b != 0:
        carry = a & b  # AND gives the carry
        a = a ^ b  # XOR gives the sum without carry
        b = carry << 1  # Shift carry to the left by 1 (carry into the next position)
  
    return a if a <= 0x7FFFFFFF else ~(a ^ 0xFFFFFFFF)  # Handle negative numbers (32-bit signed integer)

# Example test case
a = 1
b = 2
print(getSum(a, b))  # Output: 3
```

#### Time and Space Complexity:

```python
# Time Complexity: O(1), since the number of iterations is constant (a fixed number of bits in integers).

# Space Complexity: O(1), as we only use a few extra variables (a, b, carry).
```

#### Alternative Approach:

This bit manipulation approach is optimal for performing addition without using arithmetic operators. There are no better alternatives.

---

### 18. **Reverse Integer** (Medium)

#### Problem Explanation:

Given a 32-bit signed integer `x`, return `x` with its digits reversed. If reversing `x` causes the value to go outside the signed 32-bit integer range `[-2^31, 2^31 - 1]`, return 0.

#### Numeric Example:

```
Input: x = 123
Output: 321

Input: x = -123
Output: -321
```

#### Coding Pattern:

This problem can be solved using **Simple Arithmetic**. We repeatedly extract the last digit of the number, build the reverse number, and check for overflow.

#### Solution:

```python
def reverse(x):
    sign = -1 if x < 0 else 1
    x *= sign
    result = 0
  
    # Step 1: Extract digits and reverse the number
    while x:
        result = result * 10 + x % 10
        x //= 10
  
    result *= sign
  
    # Step 2: Check for overflow (32-bit signed integer range)
    if result < -2**31 or result > 2**31 - 1:
        return 0
  
    return result

# Example test case
x = 123
print(reverse(x))  # Output: 321

x = -123
print(reverse(x))  # Output: -321
```

#### Time and Space Complexity:

```python
# Time Complexity: O(log(x)), where x is the value of the input number.
# We extract the digits of x, and the number of digits is proportional to log(x).

# Space Complexity: O(1), as we only use a few extra variables (sign, result).
```

#### Alternative Approach:

This approach is optimal for reversing an integer. Other methods (e.g., converting the number to a string and reversing it) would increase space complexity.

---
