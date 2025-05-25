class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        low = 0
        high = len(s) - 1
        while low < high: # an equal index would be a unitary middle that is OK for palindromes
            if not s[low].isalnum():
                low += 1
                continue
            if not s[high].isalnum():
                high -= 1
                continue
            if s[low] != s[high]:
                return False
            low += 1
            high -= 1
        return True

"""
0p

low = 0
high = 1


alternative answer is return s == reversed(s)
"""