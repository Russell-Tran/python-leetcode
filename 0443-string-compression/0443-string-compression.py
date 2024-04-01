"""

["a","b","b","b","b","b","b","b","b","b","b","b","b"]

overwrite_index = 1
current_count = 1
i = 1


["a","a","b","b","c","c","c"]

"""
class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) < 2:
            return len(chars)
        
        chars.append("")
        overwrite_index = 1
        current_count = 1
        for i in range(1, len(chars)):
            if chars[i] == chars[i-1]:
                current_count += 1
            else:       
                if current_count > 1:
                    digits = str(current_count)
                    for digit in digits:
                        chars[overwrite_index] = digit
                        overwrite_index += 1
                        
                chars[overwrite_index] = chars[i]
                overwrite_index += 1
                current_count = 1  
        
        for _ in range(len(chars) - overwrite_index + 1):
            chars.pop()
        return overwrite_index
