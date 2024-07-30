class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # 1st approach - Get row and col
        for row in range(len(matrix)):
            target_row = row
            if target < matrix[row][0]:
                target_row = row-1
                break

        for value in matrix[target_row]:
            if value == target:
                return True
        return False
    
    # Note: Better solution available (Binary Search)