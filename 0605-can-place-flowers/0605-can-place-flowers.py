class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if not n:
            return True
        
        
        flowerbed = [0] + flowerbed + [0]
        remaining = n
        for i in range(1, len(flowerbed)-1):
            if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                # plant
                flowerbed[i] = 1
                remaining -= 1
                if remaining == 0:
                    return True
            

        return False
            