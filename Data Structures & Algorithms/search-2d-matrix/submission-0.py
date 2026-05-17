class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        n = len(matrix[0]) # 列の数（幅）
        m = len(matrix)    # 行の数（高さ）

        left_index = 0

        # right_index は「全体の最後の番号」にする
        right_index = (m * n) - 1

        while left_index <= right_index:
            # イメージ
            center = (left_index + right_index) // 2
            value = matrix[center // n][center % n]  # ← ここ！

            if value == target:
                return True
            elif value < target:
                left_index = center + 1
                continue
            right_index = center - 1
        
        return False