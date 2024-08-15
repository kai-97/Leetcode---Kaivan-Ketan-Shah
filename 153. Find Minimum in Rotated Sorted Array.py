class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return min(nums[0], nums[-1])

        if nums[0] < nums[-1]:
            return nums[0]

        start = 0
        end = len(nums)

        while start < end:
            mid = (start+end)//2
            if nums[mid] > nums[-1]:
                start = mid+1
            else:
                end = mid
        return nums[start]
    


# binary search is log n, recursion is 2**N