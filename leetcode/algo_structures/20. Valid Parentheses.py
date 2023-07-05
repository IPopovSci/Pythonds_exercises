'''Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.



Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        match={'(':')','{':'}','[':']'}
        for char in s:
            if char in match:
                stack.append(char)
            elif char in match.values() and len(stack)!=0:
                pop=stack.pop()
                if char!=match[pop]:
                    return False
            else:
                return False
        if len(stack)==0:
            return True
