class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False

        stack = []

        open_br = ['{', '[', '(']
        close_br = ['}', ']', ')']

        for chara in s:
            if chara in open_br:
                stack.append(chara)
            else:
                if not stack:
                    return False
                br = stack.pop()
                if chara == '}' and br != '{':
                    return False
                elif chara == ']' and br != '[':
                    return False
                elif chara == ')' and br != '(':
                    return False
        return True if not stack else False