class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # check if there are duplicates in each row first
        row_map = dict()
        for row in range(0, 9):
                for col in range(0, 9):
                        if board[row][col] != '.' and board[row][col] in row_map:
                                return False
                        else:
                                row_map[board[row][col]] = 1
                row_map = dict()
        # check if there any duplicates in the columns 
        col_map = dict()
        for col in range(0, 9):
                for row in range(0, 9):
                        if board[row][col] != '.' and board[row][col] in col_map:
                                return False
                        else:
                                col_map[board[row][col]] = 1
                col_map = dict()
        # break the sudoku into groups of 3x3
        # check if there are dupes in that
        
        block_map = dict()
        for i in range(0,9,3):
                for j in range(0,9,3):
                        start_row = (i // 3) * 3
                        start_col = (j // 3) * 3
                        for r in range(start_row, start_row + 3):
                                for c in range(start_col, start_col + 3):
                                        if board[r][c] != '.' and board[r][c] in block_map:
                                                return False
                                        else:
                                                block_map[board[r][c]] = 1
                        block_map = dict()
        
        return True
