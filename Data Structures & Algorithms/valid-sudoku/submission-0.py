class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # 1. 行のチェック
        for row in board:
            # 0（空白）を除いた数字だけのリストを作る
            nums = [n for n in row if n != "."]
            if len(nums) != len(set(nums)):
                return False
        # 列
        for column in zip(*board):
            # 0（空白）を除いた数字だけのリストを作る
            nums = [n for n in column if n != "."]
            if len(nums) != len(set(nums)):
                return False
        
        # Box
        for row_start in range(0, 9, 3):
            for col_start in range(0, 9, 3):
                box = []
                for index_row in range(3):
                    for index_col in range(3):
                        box.append(board[row_start + index_row][col_start + index_col])
                box_nums = [n for n in box if n != "."]
                if len(box_nums) != len(set(box_nums)):
                    return False
        return True