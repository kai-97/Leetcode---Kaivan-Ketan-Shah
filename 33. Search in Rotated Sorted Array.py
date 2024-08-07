class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def binary_search(nums_arr, target_num):
            i = 0
            j = len(nums_arr)-1
            while i<=j:
                mid = (i+j)//2
                if target_num == nums_arr[mid]:
                    return mid
                elif target_num < nums_arr[mid]:
                    j = mid-1
                elif target_num > nums_arr[mid]:
                    i = mid+1
            return -1

        if target == nums[0]:
            return 0
        if target == nums[-1]:
            return len(nums)-1
            
        index = -1
        if nums[0] > nums[-1]:
            for i in range(1, len(nums)):
                if(nums[i-1]>nums[i]):
                    index = i
                    break
        
        if index == -1:
            return binary_search(nums, target)

        if target == nums[index]:
            return index
        if target > nums[0] and target <= nums[index-1]:
            return binary_search(nums[0:index], target)
        elif target > nums[index] and target < nums[-1]:
            val = binary_search(nums[index:], target)
            return index + val if val > 0 else -1
        return -1