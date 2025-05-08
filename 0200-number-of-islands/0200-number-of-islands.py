from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seeds = {(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == "1"}
        island_count = 0
        
        while seeds:
            island_count += 1
            seed = seeds.pop()
            queue = deque([seed])

            while queue:
                i, j = curr = queue.popleft()
                directions = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
                for direction in directions:
                    if direction in seeds:
                        seeds.remove(direction)
                        queue.append(direction)

        return island_count
