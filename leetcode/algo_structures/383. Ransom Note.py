'''
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.



Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true



Constraints:

    1 <= ransomNote.length, magazine.length <= 105
    ransomNote and magazine consist of lowercase English letters.
'''

#Slow, but working:
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom=list(ransomNote)
        for i in magazine:
            if i in ransom:
                ransom.remove(i)
            if len(ransom)==0:
                return True
        return False

#Much quicker solution:
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        all_let=set(ransomNote)
        for let in all_let:
            if ransomNote.count(let)>magazine.count(let):
                return False
        return True
#Using hash:
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash_zine={}
        for i in magazine: #Init
            if i in hash_zine:
                hash_zine[i]+=1
            else:
                hash_zine[i]=1
        for i in ransomNote:
            if i not in hash_zine.keys():
                return False
            hash_zine[i]-=1
            if hash_zine[i]<0:
                return False
        return True