class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    
        # low = 0
        # high = len(matrix) * len(matrix[0]) - 1


        # while low <= high:
        #     mid = 

        # print(f"low: {low}, high: {high}")
        ROWS, COLS = len(matrix), len(matrix[0])

        low, high = 0, ROWS - 1

        while low <= high:
            mid = (low + high) // 2
            print(f"low: {low}, high: {high}, mid: {mid} ")
            if target > matrix[mid][-1]:
                low = mid + 1
            elif target < matrix[mid][0]:
                high = mid - 1
            elif target >= matrix[mid][0] and target <= matrix[mid][-1]:
                break
        
        print(f'It is in this row: {mid} for target: {target}')
        row = mid
        low, high = 0, COLS - 1

        while low <= high:
            mid = (low + high) // 2
            if target > matrix[row][mid]:
                low = mid + 1
            elif target < matrix[row][mid]:
                high = mid - 1
            elif target == matrix[row][mid]:
                return True 

        return False

        # row_l = 0 
        # row_h = len(matrix) - 1
        
        # while row_l <= row_h:
        #     mid = (row_l + row_h) // 2
        #     print(f"row_l: {row_l}, row_h: {row_h}, mid: {mid} ")
        #     print(f"matrix[mid][-1]: {matrix[mid][-1]},  matrix[row_h][-1]: {matrix[row_h][-1]}")
        #     if matrix[mid][0] >= target and matrix[mid][-1] <= target:
        #         break
        #     elif matrix[mid][-1] > matrix[row_l][-1]:
        #         row_l = mid + 1
        #     elif matrix[mid][-1] < matrix[row_h][-1]:
        #         row_h = mid - 1
        
        # print(f"Number in this row: {matrix[mid]}")
                
        # low = 0
        # high = len(matrix) * len(matrix[0]) - 1

        
        # while low <= high:
        #     mid = (low + high) // 2
        #     quoteint = mid // len(matrix)
        #     remainder = mid % len(matrix)
        #     print(f"low: {low}, high: {high}, mid: {mid}, quoteint: {quoteint}, remainder: {remainder} ")
        #     if matrix[quoteint][remainder] == target:
        #         return True
        #     elif matrix[quoteint][remainder] < target:
        #         low = mid + 1
        #     elif matrix[quoteint][remainder] > target:
        #         high = mid - 1

        # return False