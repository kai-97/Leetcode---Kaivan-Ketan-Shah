class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(existing_list, visited):
            if len(existing_list) == len(nums):
                result.append(existing_list.copy())
                return

            for value in nums:
                if value not in visited:
                    existing_list.append(value)
                    visited.add(value)
                    backtrack(existing_list, visited)
                    visited.remove(value)
                    existing_list.pop()
        
        outer_temp = nums.copy()
        visited = set()
        backtrack([], visited)
        return result