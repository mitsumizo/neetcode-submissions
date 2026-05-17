class Solution:
    def isValid(self, s: str) -> bool:
        # 閉じカッコをキーにすると、相方探しが楽になる
        mapping = {")": "(", "}": "{", "]": "["}
        stack = []

        for char in s:
            if char in mapping:
                # 閉じカッコが来た場合
                # スタックが空か、一番上が相方じゃなければ即アウト
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                # 開きカッコが来た場合はスタックに積むだけ
                stack.append(char)

        # 最後にスタックが空なら完璧（残りカスがないかチェック）
        return not stack