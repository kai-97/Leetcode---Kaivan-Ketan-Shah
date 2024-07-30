class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        ### My Solution Attempt -> TLE
        # max_res = max(nums)

        # for window_size in range(2, len(nums)+1):
        #     for start in range(len(nums)):
        #         end = (start + window_size - 1)%len(nums)
        #         if end < start:
        #             max_res = max(max_res, sum(nums[start:]) + sum(nums[:end+1]))
        #         else:
        #             max_res = max(max_res, sum(nums[start:end+1]))
        # return max_res


        ## Kadane's Algo - Better Code Quality Than one below
        max_so_far = float('-inf')
        max_current = 0

        for n in nums:
            max_current += n
            max_so_far = max(max_so_far, max_current)
            max_current = max(max_current, 0)

        min_so_far = float('inf')
        min_current = float('inf')

        for n in nums:
            min_current += n
            min_so_far = min(min_so_far, min_current)
            min_current = min(min_current, 0)

        return max(max_so_far, sum(nums)-min_so_far)





        ### Solution using Kadane's Algorithm
        max_so_far = float('-inf')
        min_so_far = float('inf')
        max_ending_here = 0
        min_ending_here = float('inf')

        # Calculating max in the contiguous sub-array
        for i in range(len(nums)):
            max_ending_here += nums[i]
            if max_ending_here > max_so_far:
                max_so_far = max_ending_here
            if max_ending_here < 0:
                max_ending_here = 0
        
        # Calculating min in the contiguous sub-array
        #for i in range(len(nums)):
            min_ending_here += nums[i]
            if min_ending_here < min_so_far:
                min_so_far = min_ending_here
            if min_ending_here > 0:
                min_ending_here = 0

        # Returning max(max_calculated, total_sum - min_calculated)
        return max(max_so_far, sum(nums)-min_so_far)