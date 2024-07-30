class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []    
        def dfs (open: int, close: int, s: str):
            if open == close and (open + close)==2*n:
                res.append(s)
                return
            if open < n:
                dfs(open+1, close, s + "(")
            if close < open:
                dfs(open, close+1, s+")")

        dfs(0, 0, "")

        return res