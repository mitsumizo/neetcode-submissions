class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 上下左右をデータ化

        def dfs(r, c, i, visited):
            # board[r][c] == word[i] が成立してる前提で呼ばれる
            if i == len(word) - 1:        # 最後の文字まで揃った → 成功
                return True

            for dr, dc in DIRECTIONS:     # 4方向を1つのループで
                nr, nc = r + dr, c + dc
                if (0 <= nr < rows and 0 <= nc < cols       # 盤面の中？
                        and (nr, nc) not in visited          # まだ踏んでない？
                        and board[nr][nc] == word[i + 1]):   # 次の文字と一致？
                    visited.add((nr, nc))
                    if dfs(nr, nc, i + 1, visited):
                        return True                # 成功したら即True（戻さない）
                    visited.remove((nr, nc))       # 失敗したら戻す（バックトラック）
            return False

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0] and dfs(r, c, 0, {(r, c)}):
                    return True
        return False