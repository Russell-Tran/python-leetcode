class Solution:

    def isPalindrome(self, x: int) -> bool:
        
        """
        x = 121
        output: true

        x = -121
        output: false
        """
        return self._isPalindrome(str(x))

    def _isPalindrome(self, x: str) -> bool:
        
        """
        x = 121
        output: true

        x = -121
        output: false
        """
        if not x or len(x) == 1:
            return True
        if x[0] != x[-1]:
            return False
        return self._isPalindrome(x[1:-1])

        