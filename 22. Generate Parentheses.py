class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(open, close, bracket_string):
            if open == 0 and close == 0:
                res.append(bracket_string)
                return
            if close > 0 and close > open:
                dfs(open, close-1, bracket_string+')')
            if open > 0:
                dfs(open-1, close, bracket_string+'(')
        dfs(n, n, "")
        return res
        