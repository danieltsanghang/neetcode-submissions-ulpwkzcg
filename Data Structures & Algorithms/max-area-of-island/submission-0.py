class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    area = search((i,j), grid)
                    ans = max(ans, area)
                    print(area, ans)
        return ans

        

def search(cell, grid):
    x,y = cell[0], cell[1]
    if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == 0:
        return 0
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    counter = 1
    grid[x][y] = 0
    for d in directions:
        nx, ny = x+d[0], y+d[1]
        counter += search((nx, ny), grid)
    return counter