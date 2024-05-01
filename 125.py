class Solution:
    def isPalindrome(self, s: str) -> bool:
        # create my own alphanum
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

    @staticmethod
    def isalnum(c):
        return ord('A')<= ord(c) <= ord('Z') or ord('a') <= ord(c) <ord('z') or ord(1) <= ord(c) <ord(9)

    '''
    Time complexity: O(n), space complexity: O(1)
    Used two pointers to check if the string is palindrome:
        - used a while loop to check if the characters are alphanumeric while maintaining the l < r condition.  
    '''