from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seeds = {(i,j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j]}
        maximum_area = 0

        while seeds:
            seed = seeds.pop()
            area = 1
            queue = deque([seed])
            while queue:
                i, j = queue.popleft()
                directions = [
                    (i-1, j),
                    (i+1, j),
                    (i, j-1),
                    (i, j+1)
                ]
                for direction in directions:
                    if direction in seeds:
                        seeds.remove(direction)
                        area += 1
                        queue.append(direction)
            maximum_area = max(area, maximum_area)

        return maximum_area