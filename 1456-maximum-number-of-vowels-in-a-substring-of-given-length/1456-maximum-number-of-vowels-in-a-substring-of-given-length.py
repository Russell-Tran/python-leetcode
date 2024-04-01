class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        if not s:
            return 0
        
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        most = 0
        vowel_count = 0 
        
        for char in s[:k]:
            if char in vowels:
                vowel_count += 1
        
        most = max(most, vowel_count)
        
        if len(s) <= k:
            return most
        
        window_offset = k - 1
        for i in range(1, len(s) - k + 1):
            if s[i-1] in vowels:
                vowel_count -= 1
            if s[i+window_offset] in vowels:
                vowel_count += 1
            most = max(most, vowel_count)
        
        return most
        
        
        
        
        
        
        
        
        
        
        
#         if not s:
#             return 0
#         vowels = set(['a', 'e', 'i', 'o', 'u'])
#         most = 0
#         consecutive = 0
#         if s[0] in vowels:
#             consecutive += 1
#             most = max(most, consecutive)
        
#         for char in s[1:]:
#             if char in vowels:
#                 consecutive += 1
#             else:
#                 most = max(most, consecutive)
#                 consecutive = 0
        
#         most = max(most, consecutive)
#         return min(k, most)