# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
#  An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
# You may assume all four edges of the grid are all surrounded by water.
# Example 1:

# Input:
# 11110
# 11010
# 11000
# 00000

# Output: 1
# Example 2:

# Input:
# 11000
# 11000
# 00100
# 00011

# Output: 3


class IslandProblem_dfs(object):
    def numIslands(self, grid):
        #         return if grid is empty
        if len(grid) == 0:
            return 0

        result = 0
        # iterate each matrix
        for i, i_row in enumerate(grid):
            for j, value in enumerate(i_row):

                        #    we only care about the land aka '1'
                if value == '1':
                    result += self.dfs(grid, i, j)
        return result

    def dfs(self, grid, i, j):
        # Check if the current index is valid and not sunked
        if(i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]) or grid[i][j] == '0'):
            return 0

        # let the island sink ;)
        grid[i][j] = '0'

        # iterate neighbours
        self.dfs(grid, i-1, j)
        self.dfs(grid, i+1, j)
        self.dfs(grid, i, j-1)
        self.dfs(grid, i, j+1)
        return 1
