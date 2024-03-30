class Solution:
    def reverseWords(self, s: str) -> str:
        if not s:
            return s
        
        return " ".join(reversed([word for word in s.split(" ") if word]))