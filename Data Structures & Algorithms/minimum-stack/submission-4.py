class MinStack:
    def __init__(self):
        self.stack = []
        # 各ステップでの「最小値」を記録するためのスタック
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        # min_stack が空、もしくは新しい値が現在の最小値以下なら更新
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        else:
            # 現在の最小値を維持して追加（常に stack と高さを合わせる方法もあるけど、今回は最小値が更新された時だけ積むやり方でいくね）
            # ※pop時に整合性をとる必要がある
            pass

    # --- 上記の「高さを合わせる（冗長だけど安全な）」やり方で書き直すね ---
    def push(self, val: int) -> None:
        self.stack.append(val)
        # 現在の最小値を計算して min_stack に積む
        current_min = val
        if self.min_stack:
            current_min = min(val, self.min_stack[-1])
        self.min_stack.append(current_min)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]