import math
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # setup
        n = len(matrix)
        
        
        # Collect the onion cells of one corner
        onion_cells = []
        for i in range(n // 2 + n % 2): # notice this setup
            for j in range(n // 2):     # notice this setup
                onion_cells.append((i,j))
        
        
        
        # Do in-place rotational behavior
        
        for onion_cell in onion_cells:
            i, j = onion_cell
            current_val = matrix[i][j]
            
            # 1. displace top to right (aka clockwise rotation)
            # distance from top becomes distance from right
            distance_from_right = distance_from_top = i
            # distance from left becomes distance from top 
            distance_from_top = distance_from_left = j
            new_i = distance_from_top
            new_j = (n-1) -  distance_from_right
            
            i, j = new_i, new_j
            temp = matrix[i][j]
            matrix[i][j] = current_val
            current_val = temp
            
            # 2. displace right to bottom
            # distance from right becomes distance from bottom
            distance_from_bottom = distance_from_right = (n-1) - j
            # distance from top becomes distance from right
            distance_from_right = distance_from_top = i
            
            new_i = (n-1) - distance_from_bottom
            new_j = (n-1) - distance_from_right
            
            i, j = new_i, new_j
            temp = matrix[i][j]
            matrix[i][j] = current_val
            current_val = temp
            
            # 3. displace bottom to left
            # distance from bottom becomes distance from left
            distance_from_left = distance_from_bottom = (n-1) - i
            # distance from right becomes distance from bottom
            distance_from_bottom = distance_from_right = (n-1) - j
            
            new_i = (n-1) - distance_from_bottom
            new_j = distance_from_left
            
            i, j = new_i, new_j
            temp = matrix[i][j]
            matrix[i][j] = current_val
            current_val = temp
            
            # 4. displace left to top
            # distance from left becomes distance from top
            distance_from_top = distance_from_left = j
            # distance from bottom becomes difference from left
            distance_from_left = distance_from_bottom = (n-1) - i
            
            new_i = distance_from_top
            new_j = distance_from_left
            
            i, j = new_i, new_j
            temp = matrix[i][j]
            matrix[i][j] = current_val
            current_val = temp
            
        return
        
            

        
"""

junk



            # distance from top becomes distance from right
            # distance from left becomes distance from top             
            new_i = j
            new_j = (n-1) - i
            
            
            
            # 1. displace top to right (aka clockwise rotation)
            # distance from top becomes distance from right
            distance_from_right = distance_from_top = i
            # distance from left becomes distance from top 
            distance_from_top = distance_from_left = j
            new_i = distance_from_top
            new_j = (n-1) -  distance_from_right
            
            
            if face == 0:
        
            # distance from top becomes distance from right
            
            # distance from left becomes distance from top 
        
            elif face == 1:

                # distance from right becomes distance from bottom

                # distance from top becomes distance from right

            elif face == 2:

                # distance from bottom becomes distance from left

                # distance from right becomes distance from bottom

            else: # face == 3

                # distance from left becomes distance from top

                # distance from bottom becomes difference from left

            face += 1
            if face >= 4:
                # move to next cell in the collection of onion layers

            face %= 4
            
            
            
            
            # setup
        n = len(matrix)
        midpoint = n // 2 # who cares if it's odd because a single center cell stays put
        
        
        # Collect the onion cells of one face
        onion_cells = []
        i = 0
        while i <= midpoint:
            layer = [(i, j) for j in range(i, n-i)]
            onion_cells += layer
            i+= 1
"""
        