class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        worddict = set(wordDict)
        result = [False]*(len(s)+1)
        result[0] = True

        for i in range(1, len(s)+1):
            for j in range(i):
                if result[j] and s[j:i] in wordDict:
                    result[i] = True
                    break
        return result[-1]