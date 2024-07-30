class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # Hint - Use DP. Came up solution myself.

        
        dp = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]
        dp[0][0] = grid[0][0]

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if i == 0 and j > 0:
                    dp[i][j] = grid[i][j] + dp[i][j-1]
                elif j == 0 and i > 0:
                    dp[i][j] = grid[i][j] + dp[i-1][j]
                elif i > 0 and j > 0:
                    dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]