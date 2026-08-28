class Solution:
    def isValidSudoku(self, board) -> bool:
        col_dup = {} # {1: [3,,,2,2,2,]}
        squares = {}
        row_dup = {}
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == ".":
                    continue
            

                row_l = row_dup.get(row, [])
                col_l = col_dup.get(col, [])
                square_l = squares.get((row // 3, col // 3), [])
                value = board[row][col]
        
                if value in row_l or value in col_l or value in square_l:
                    return False
                
                row_l.append(board[row][col])
                col_l.append(board[row][col])
                square_l.append(board[row][col])
                
                row_dup[row] = row_l
                col_dup[col] = col_l
                squares[(row // 3, col // 3)] = square_l
        return True
