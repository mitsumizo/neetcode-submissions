class Solution:

    def find_next_word(self, word):
        return word[1:] if len(word) > 1 else ""

    def search(self, board, word, current_point_row_index, current_point_col_index, paths):
        """
            上下左右だけ探すことに特化したメソッド。
            input: 
                board : 2-D grid of character
                word : 探すべき単語（最初の文字がターゲット）空文字 = 探すものがない
                current_point_row_index : 現在見ている行のインデックスの位置
                current_point_col_index : 現在見ている列のインデックスの位置
            
            output:
                boolean : 存在したか否か
        """

        # 上下左右
        return_result = [False,False,False,False]

        if len(word) == 0:
            return True

        # 上を探す（あれば）かつ 通ったことない
        if current_point_row_index > 0:
            target_row_index = current_point_row_index - 1
            if (target_row_index, current_point_col_index) not in paths and word[0] == board[target_row_index][current_point_col_index]:
                paths.append((target_row_index, current_point_col_index))
                return_result[0] = self.search(board, self.find_next_word(word), target_row_index, current_point_col_index, paths)
                if not return_result[0]:
                    paths.pop()

        # 下を探す（あれば）
        if current_point_row_index < len(board) - 1:
            target_row_index = current_point_row_index + 1
            if (target_row_index, current_point_col_index) not in paths and word[0] == board[target_row_index][current_point_col_index]:
                paths.append((target_row_index, current_point_col_index))
                return_result[1] = self.search(board, self.find_next_word(word), target_row_index, current_point_col_index, paths)
                if not return_result[1]:
                    paths.pop()

        # 左を探す（あれば）
        if current_point_col_index > 0:
            target_col_index = current_point_col_index - 1
            if (current_point_row_index, target_col_index) not in paths and word[0] == board[current_point_row_index][target_col_index]:
                paths.append((current_point_row_index, target_col_index))
                return_result[2] = self.search(board, self.find_next_word(word), current_point_row_index, target_col_index, paths)
                if not return_result[2]:
                    paths.pop()

        # 右を探す（あれば）
        if current_point_col_index < len(board[0]) - 1:
            target_col_index = current_point_col_index + 1
            if (current_point_row_index, target_col_index) not in paths and word[0] == board[current_point_row_index][target_col_index]:
                paths.append((current_point_row_index, target_col_index))
                return_result[3] = self.search(board, self.find_next_word(word), current_point_row_index, target_col_index, paths)
                if not return_result[3]:
                    paths.pop()

        return True in return_result



    def exist(self, board: List[List[str]], word: str) -> bool:

        for row_index in range(len(board)):
            for row_col in range(len(board[row_index])):
                answer = False
                if board[row_index][row_col] == word[0]:
                    answer = self.search(board, self.find_next_word(word), row_index, row_col, [(row_index, row_col)])
                
                if answer:
                    return True

        return False

        # 1. TARGETの単語を探す
        
        # 1.1 見つかった場合
            # 1.1.1 次の単語を上下左右 で探す をTARGETの文字
            # 1.1.2 見つかったら、単語をずらして1.1に戻る
            # 1.1.3 見つからなかったら、諦める
            # 1.1.4 次の単語がなくなった（全ての単語がソロった）場合はresultに追加

        # 1.2 見つからなかった場合
            # 次の場所へ

