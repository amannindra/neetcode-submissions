class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        s = {}
        k = {}
        start = 0
        end = 3
        for i in range(len(board)):
            l = set()
            for j in range(len(board[0])):
                if (board[i][j] != "."):
                    if str(j) not in s:
                        s[str(j)] = set(board[i][j])
                    else: 
                        if (board[i][j] in s[str(j)]):
                            print(f"board[i][j]: {board[i][j]} in s: {s}")
                            return False
                        else:
                            col = s[str(j)]
                            col.add(board[i][j])
                            s[str(j)] = col
                
                    square = (i // 3) * 3 + j // 3
                    if str(square) not in k:
                        k[str(square)] = set(board[i][j])
                    else:
                        if board[i][j] in k[str(square)]:
                            print(f"board[i][j]: {board[i][j]} in k")
                            return False

                    if (board[i][j] in l):
                        print(f"board[i][j]: {board[i][j]} in l: {l}")
                        return False
                    else:
                        l.add(board[i][j])   
            print(f"l: {l}")
            print(f"s: {s}")
            print(f"k: {k}")
            print('________________')
    
        return True


        