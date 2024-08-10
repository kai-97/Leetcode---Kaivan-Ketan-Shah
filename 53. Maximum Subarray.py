class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        curr_max = float('-inf')
        overall_max = float('-inf')

        for n in nums:
            curr_max = max(n, curr_max+n)
            overall_max = max(overall_max, curr_max)
        return overall_max