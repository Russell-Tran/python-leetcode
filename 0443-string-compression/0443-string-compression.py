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
                if 1 < current_count and current_count < 10:
                    chars[overwrite_index] = str(current_count)
                    overwrite_index += 1
                else: # current count >= 10
                    
                    # need to do maneuver to store the digits, 
                    # go back to front s.t. most significant digit ends up first
                    digits = 0
                    ct = current_count
                    while ct > 0:
                        digits += 1
                        ct //= 10
                    ct = current_count
                    back = 1
                    while ct > 0:
                        char[overwrite_index + digits - back] = str(ct % 10)
                        ct //= 10
                        back += 1
                    overwrite_index += digits
                    
                chars[overwrite_index] = chars[i]
                overwrite_index += 1
                current_count = 1
                
        chars.pop()
        return overwrite_index
    """