class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:        
        
        if not matrix:
            return False

        # First Binary Search on the cols to get the row index
        first_col = [row[0] for row in matrix]
        start = 0
        end = len(first_col)-1
        while start <= end:
            mid = (start+end)//2
            if first_col[mid] == target:
                return True
            elif target < first_col[mid]:
                end = mid-1
            elif target > first_col[mid]:
                start = mid+1

        # Second Binary Search on the selected row to check for number existence
        row = matrix[end]
        start = 0
        end = len(row)-1
        while start <= end:
            mid = (start+end)//2
            if row[mid] == target:
                return True
            if target > row[mid]:
                start = mid + 1
            elif target < row[mid]:
                end = mid - 1
        return False