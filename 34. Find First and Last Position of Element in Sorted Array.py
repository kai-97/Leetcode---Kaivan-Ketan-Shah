class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n == 0:
            return [-1,-1]

        if n == 1:
            if target == nums[0]:
                return [0, 0]
            return [-1,-1]
        
        if nums[0] == target:
            right = 0
            while right < n and target == nums[right]:
                right += 1
            return [0, right-1]

        if nums[-1] == target:
            left = n-1
            while left >= 0 and nums[left] == target:
                left -= 1
            return [left + 1, n-1]

        start = 0
        end = n-1
        mid = (start+end)//2

        while start <= end:
            mid = (start+end)//2
            
            if nums[mid] == target:
                left = mid
                right = mid

                while nums[left] == target:
                    left -= 1
                while nums[right] == target:
                    right += 1
                return [left+1, right-1]
                
            if target > nums[mid]:
                start = mid + 1
            else:
                end = mid - 1
        return [-1, -1]