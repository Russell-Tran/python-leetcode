class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split(" ")
        for word in reversed(words):
            if word:
                return len(word)
       
    def lengthOfLastWord(self, s: str) -> int:
        last = s.rsplit(maxsplit=1)[-1]
        return len(last)
            
    """
    
    class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last = s.rsplit(maxsplit=1)[-1]
        return len(last)
        
    
    """