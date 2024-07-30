class Solution:
    def climbStairs(self, n: int) -> int:
    
        # Recursion - 1st attempt
        # if n == 1 or n == 2:
        #     return n
        # return self.climbStairs(n-1) + self.climbStairs(n-2)

        # Memoization - Hint
        # memo = {0:1, 1:1}
        # for i in range(2, n+1):
        #     memo[i] = memo[i-1] + memo[i-2]
        # return memo[n]

        # Fib style approach - Thought out myself
        prev_2, prev_1, current = 1, 1, 1
        counter = 2

        while counter != n+1:
            current = prev_1 + prev_2
            prev_2 = prev_1
            prev_1 = current

            counter += 1
        return current