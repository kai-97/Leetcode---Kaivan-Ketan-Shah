class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:        
        start = 0
        end = len(matrix)-1
        index = 0

        while start <= end:
            mid = (start + end)//2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                index = mid
                break
            if target > matrix[mid][0]:
                start = mid + 1
            elif target < matrix[mid][0]:
                end = mid - 1

        row = matrix[index]
        start = 0
        end = len(row)-1
        while start <= end:
            mid = (start+end)//2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                start = mid+1
            elif row[mid] > target:
                end = mid-1
        return False