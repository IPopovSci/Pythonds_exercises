'''Given an integer x, return true if x is a
palindrome
, and false otherwise.



Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.



Constraints:

    -231 <= x <= 231 - 1


Follow up: Could you solve it without converting the integer to a string?'''

#Without using string:
class Solution:
    def isPalindrome(self, x: int) -> bool:

        num_list = []
        if x < 0:
            return False
        # Converting int to list without using string:
        while x > 0:
            num_list.insert(0, x % 10)
            x = x // 10
        for i in range(len(num_list) // 2):
            print(i)
            if num_list[i] != num_list.pop():
                return False
        return True
#Using string:
class Solution:
    def isPalindrome(self, x: int) -> bool:
      return str(x)[::-1]==str(x) #Checks if inverted string equals to original