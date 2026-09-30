# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise

# s = ''.join(c.lower() for c in s if c.isalnum())
# s == s[::-1]

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left=0
        right=len(s)-1
        while left<right:
            
            while left<right and not s[left].isalnum():   #isalnum() method checks whether the string consists of alphanumeric characters or not. It returns True if all characters in the string are alphanumeric, otherwise it returns False. 
                left+=1
            while left<right and not s[right].isalnum():
                right-=1
            while s[right].lower() !=s[left].lower():  #lower()is a method
                return False
            left+=1
            right-=1
        return True

            