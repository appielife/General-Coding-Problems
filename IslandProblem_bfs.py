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


from collections import deque 

class Solution(object):
    def numIslands(self, grid):
#         return if grid is empty
        if len(grid) == 0:
            return 0        
        result=0
        queue= deque()
        for i_, i_row in enumerate(grid):
            for j_, value in enumerate(i_row): 
                if grid[i_][j_] =='1':                                      
                    queue.append((i_,j_))
                    result+=1                              
                    while queue:
                        q = queue.popleft()
                        i=q[0]
                        j=q[1]  
                        if(i<0 or j<0 or i >=len(grid) or j >=len(grid[i]) or grid[i][j] == '0' ):
                            continue
                        grid[i][j]='0' 
                        queue.append((i-1,j))
                        queue.append((i+1,j))
                        queue.append((i,j-1))
                        queue.append((i,j+1))              
        return result  

                
        
        
        """
        :type grid: List[List[str]]
        :rtype: int
        """


# Runtime: 132 ms, faster than 61.60% of Python online submissions for Number of Islands.
# Memory Usage: 19 MB, less than 62.16% of Python online submissions for Number of Islands.        