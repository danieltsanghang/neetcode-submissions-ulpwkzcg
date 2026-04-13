class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '0':
                    continue
                else:
                    islands += 1
                    dfs((i,j), grid)
        return islands
                
def dfs(current, grid):
    # print('explore', current)
    if 0 > current[0] or current[0] >= len(grid) or 0 > current[1] or current[1] >= len(grid[0]) or grid[current[0]][current[1]] == '0':
        return 
    else:
        directions = [(-1, 0), (1,0), (0, -1), (0, 1)]
        grid[current[0]][current[1]] = '0'
        for d in directions:
            c = d[0]
            r = d[1]
            dfs((current[0]+c, current[1]+r), grid)
        return 
