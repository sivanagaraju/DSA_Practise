"""
202. Happy Number


Description
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

 

Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
Example 2:

Input: n = 2
Output: false
 
"""

def isHappy(num):
    # to the total sum correctly we should use the below method
    """
    The helper function will find the last digit of the given number by taking its modulus with 10. 
    We’ll store this in a variable digit. Now, since we’ve already separated the last digit, we can get 
    the remaining digits by dividing the number by 10. Lastly, we’ll store the squared sum of digit in a 
    variable named total_sum. We’ll repeat this until our number becomes 0.
    
    19 is number 
    
    First Iteration:
    
        digit = 19 % 10 = 9
        number = 19/10 = 1 (remaining digit(s))
        total_sum = 9 ** 2 =  81
    
    Second Iteration:

        digit = 1 % 10  = 1 (last digit)
        number = 1/ 10  = 0 (remaining digits(s))
        total_sum = 81 + 1 ** 2  = 82
    
    As the number has become 0, we’ll terminate our program here. The squared sum of the digits in 19 is 82.
    """
    def next(number):
        total_sum = 0
        while number > 0:
            number, digit = divmod(number, 10)
            total_sum += digit ** 2
        return total_sum
    
    slow, fast = num, next(num)
    
    while slow != fast:
        slow, fast = next(slow), next(next(fast))
    return slow == 1

inputs = [2, 1, 5, 19, 25, 7]
for i in range(len(inputs)):
    print(f"is {i} happy number", isHappy(i))