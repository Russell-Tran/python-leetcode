import math
class Solution:
    def get_query(self, query, intLength):
        if query <= 1:
            return 
        if query <= 1 + 9:
            return 
        
        if query <= 1 + 9 + 9 * 10:
            return
        if query <= 1 + 9 + 9 * 10 + 9 * 10 * 10:
            return
    
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        output = []
        origin = 10 ** (int(math.ceil(intLength / 2)) - 1)
        for query in queries:
            front_half = str(origin + query - 1)
            middle = ""
            if intLength % 2 == 1:
                middle = front_half[-1]
                front_half = front_half[:-1]
            back_half = front_half[::-1]
            value = front_half + middle + back_half
            output.append(int(value)) if len(value) == intLength else output.append(-1)
            
        return output
        
    """
    [1,2,3,4,5,90]
    3
    
    origin = 10 ** 2 = 100
    front_half = 101
    middle = "0"
    back_half
    
    """