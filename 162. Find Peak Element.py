class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        # Approach 2 (O(logn))
        l, r = 0, len(nums)-1
        while l<r:
            mid = (l+r)//2

            if nums[mid+1] > nums[mid]:
                l = mid+1
            else:
                r = mid
        return l

        # Approach - 1 (Decent performance, not O(logn))
        # for start in [0,1]:
        #     for i in range(start,len(nums),2):
        #         prev = float('-inf') if i == 0 else nums[i-1]
        #         nex = float('-inf') if i == len(nums)-1 else nums[i+1]
        #         if nums[i] > prev and nums[i] > nex:
        #             return i