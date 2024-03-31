class Solution:
    def reverseVowels(self, s: str) -> str:
        if not s:
            return s
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        indices = []
        letters = []
        for i in range(len(s)):
            char = s[i]
            if char in vowels:
                indices.append(i)
                letters.append(char)
        
        indices = indices
        letters = reversed(letters)
        s = list(s)
        for index, letter in zip(indices, letters):
            s[index] = letter
        return "".join(s)
        